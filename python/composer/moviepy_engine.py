import os
import math
import time
import shutil
import hashlib
import tempfile
import threading
import subprocess

from moviepy import (
    VideoFileClip,
    AudioFileClip,
    TextClip,
    CompositeVideoClip,
    CompositeAudioClip,
    concatenate_videoclips,
    vfx,
    afx,
)


class MoviePyEngine:

    _font_cache = None
    _hw_encoder_cache = None
    _cache_lock = threading.Lock()

    def __init__(self):

        self.target_width = 1080
        self.target_height = 1920

        self.font_size = 60
        self.color = "white"
        self.stroke_color = "black"
        self.stroke_width = 3
        self.margin = 120

        self.caption_font_size = 100
        self.caption_color = "#FFD700"
        self.caption_stroke_color = "black"
        self.caption_stroke_width = 6

        self.crossfade_duration = 0.4
        self.zoom_strength = 0.18
        self.pan_zoom = 1.3
        self.caption_pop_duration = 0.35

        self.fps = 30
        self.default_scene_duration = 5.0
        self.min_scene_duration = 1.0

        self.sync_tolerance = 0.05

        self.ffmpeg_bin = shutil.which("ffmpeg") or "ffmpeg"
        self.ffprobe_bin = shutil.which("ffprobe") or "ffprobe"
        self.cpu_count = os.cpu_count() or 4

        self.cache_dir = os.path.join(
            tempfile.gettempdir(),
            "ai_automation_scene_cache",
        )
        os.makedirs(self.cache_dir, exist_ok=True)

        self.font = self._resolve_font_cached()
        self.hw_encoder = self._detect_hardware_encoder_cached()

        self._text_clip_cache = {}

    # ===================================================
    # FONT RESOLUTION (cached once per process)
    # ===================================================

    @classmethod
    def _resolve_font_cached(cls):

        if cls._font_cache is not None:
            return cls._font_cache

        with cls._cache_lock:
            if cls._font_cache is None:
                cls._font_cache = cls._resolve_font_impl()

        return cls._font_cache

    @staticmethod
    def _resolve_font_impl():

        preferred_names = [
            "DejaVuSans-Bold.ttf",
            "Poppins-Bold.ttf",
            "arialbd.ttf",
            "Arial Bold.ttf",
            "LiberationSans-Bold.ttf",
            "NotoSans-Bold.ttf",
        ]

        search_dirs = [
            "/usr/share/fonts",
            "/usr/local/share/fonts",
            os.path.expanduser("~/.fonts"),
            os.path.expanduser("~/.local/share/fonts"),
            "C:\\Windows\\Fonts",
            "/Library/Fonts",
            "/System/Library/Fonts",
        ]

        for directory in search_dirs:
            if not os.path.isdir(directory):
                continue
            for root, _, files in os.walk(directory):
                for name in preferred_names:
                    if name in files:
                        return os.path.join(root, name)

        for directory in search_dirs:
            if not os.path.isdir(directory):
                continue
            for root, _, files in os.walk(directory):
                for file_name in files:
                    if file_name.lower().endswith((".ttf", ".otf")):
                        return os.path.join(root, file_name)

        raise RuntimeError(
            "No usable font (.ttf/.otf) found on this system. "
            "Install a font package such as 'fonts-dejavu-core' "
            "(Ubuntu: apt-get install -y fonts-dejavu-core), or on "
            "Windows ensure C:\\Windows\\Fonts contains a .ttf file."
        )

    # ===================================================
    # HARDWARE ENCODER DETECTION (cached once per process)
    # Intel QSV -> Intel VAAPI -> libx264 (CPU) fallback.
    # ===================================================

    def _detect_hardware_encoder_cached(self):

        cls = type(self)

        if cls._hw_encoder_cache is not None:
            return cls._hw_encoder_cache

        with cls._cache_lock:
            if cls._hw_encoder_cache is None:
                cls._hw_encoder_cache = self._detect_hardware_encoder_impl()

        return cls._hw_encoder_cache

    def _detect_hardware_encoder_impl(self):

        trial_cmd_qsv = [
            self.ffmpeg_bin, "-y", "-f", "lavfi",
            "-i", "testsrc=size=320x240:duration=0.5",
            "-c:v", "h264_qsv", "-f", "null", "-",
        ]

        try:
            result = subprocess.run(
                trial_cmd_qsv,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=15,
            )
            if result.returncode == 0:
                return {"codec": "h264_qsv", "type": "qsv"}
        except Exception:
            pass

        vaapi_device = "/dev/dri/renderD128"

        if os.path.exists(vaapi_device):

            trial_cmd_vaapi = [
                self.ffmpeg_bin, "-y",
                "-vaapi_device", vaapi_device,
                "-f", "lavfi", "-i", "testsrc=size=320x240:duration=0.5",
                "-vf", "format=nv12,hwupload",
                "-c:v", "h264_vaapi", "-f", "null", "-",
            ]

            try:
                result = subprocess.run(
                    trial_cmd_vaapi,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=15,
                )
                if result.returncode == 0:
                    return {
                        "codec": "h264_vaapi",
                        "type": "vaapi",
                        "device": vaapi_device,
                    }
            except Exception:
                pass

        return {"codec": "libx264", "type": "software"}

    # ===================================================
    # LOAD VIDEO / AUDIO
    # ===================================================

    def load_video(self, path):
        return VideoFileClip(path)

    def load_audio(self, path):
        return AudioFileClip(path)

    # ===================================================
    # SCENE DURATION PARSING
    # ===================================================

    def parse_scene_duration(self, duration_value):

        if isinstance(duration_value, (int, float)):
            length = float(duration_value)
            return 0.0, length, max(length, self.min_scene_duration)

        text = str(duration_value or "").lower()
        text = text.replace("seconds", "").replace("second", "")
        text = text.replace("sec", "").strip()

        try:
            if "-" in text:
                start_text, end_text = text.split("-", 1)
                start = float(start_text.strip())
                end = float(end_text.strip())
                length = end - start
            else:
                start = 0.0
                length = float(text.strip())
                end = length

            if length <= 0:
                length = self.default_scene_duration
                end = start + length

            return start, end, max(length, self.min_scene_duration)

        except (ValueError, AttributeError):
            return 0.0, self.default_scene_duration, self.default_scene_duration

    # ===================================================
    # NORMALIZE SCENE TIMINGS TO MATCH VOICE DURATION
    # ===================================================

    def normalize_scene_timings(self, scenes, total_duration):

        parsed = []

        for scene in scenes:
            _, _, length = self.parse_scene_duration(scene.get("duration"))
            parsed.append(length)

        raw_total = sum(parsed)

        if raw_total <= 0:
            count = max(len(scenes), 1)
            parsed = [total_duration / count for _ in scenes]
            raw_total = total_duration

        scale = total_duration / raw_total if raw_total > 0 else 1.0

        timings = []
        cursor = 0.0

        for length in parsed:
            scaled = max(length * scale, 0.3)
            timings.append(
                {
                    "start": cursor,
                    "end": cursor + scaled,
                    "duration": scaled,
                }
            )
            cursor += scaled

        if timings:
            drift = total_duration - timings[-1]["end"]
            timings[-1]["end"] += drift
            timings[-1]["duration"] += drift

        return timings

    def _compute_scene_timings(self, scenes, total_duration):

        fade_count = sum(
            1
            for index, scene in enumerate(scenes)
            if index > 0
            and str(scene.get("transition", "")).strip().lower() == "fade"
        )

        planned_overlap = self.crossfade_duration * fade_count

        timings = self.normalize_scene_timings(
            scenes,
            total_duration + planned_overlap,
        )

        return timings

    # ===================================================
    # RESIZE / CROP (legacy per-frame path for no-scenes fallback)
    # ===================================================

    def resize_to_target(self, clip):

        clip = clip.resized(height=self.target_height)

        if clip.w < self.target_width:
            clip = clip.resized(width=self.target_width)

        clip = clip.cropped(
            x_center=clip.w / 2,
            y_center=clip.h / 2,
            width=self.target_width,
            height=self.target_height,
        )

        return clip

    def fit_clip_to_duration(self, clip, duration):

        if clip.duration is None or clip.duration <= 0:
            raise ValueError("Source video has invalid duration")

        if clip.duration >= duration:
            return clip.subclipped(0, duration)

        loops_needed = math.ceil(duration / clip.duration)
        looped = concatenate_videoclips([clip] * loops_needed, method="compose")

        return looped.subclipped(0, duration)

    # ===================================================
    # FFMPEG SCENE PREPROCESSING
    # ===================================================

    def _cache_key(self, video_path, duration, animation):

        try:
            stat = os.stat(video_path)
            fingerprint = f"{video_path}|{stat.st_size}|{stat.st_mtime}"
        except OSError:
            fingerprint = video_path

        fingerprint += f"|{round(duration, 2)}|{animation or 'none'}"
        fingerprint += f"|{self.target_width}x{self.target_height}|{self.fps}"

        digest = hashlib.sha1(fingerprint.encode("utf-8")).hexdigest()

        return os.path.join(self.cache_dir, f"scene_{digest}.mp4")

    def _build_scene_filter(self, animation, duration):

        animation = (animation or "").strip().lower()
        total_frames = max(int(round(duration * self.fps)), 1)

        # Two-pass scale: first fit by the constraining dimension,
        # then guarantee minimum 1080w AND 1920h before crop.
        # Prevents "Invalid argument" crop failure on any source
        # resolution — small, portrait, landscape, or 4K.
        base = (
            f"scale=w='if(gt(iw/ih,{self.target_width}/{self.target_height}),"
            f"trunc(oh*a/2)*2,{self.target_width})':"
            f"h='if(gt(iw/ih,{self.target_width}/{self.target_height}),"
            f"{self.target_height},trunc(ow/a/2)*2)',"
            f"scale=w='max(iw,{self.target_width})':h='max(ih,{self.target_height})',"
            f"crop={self.target_width}:{self.target_height}"
        )

        if animation == "zoom in":
            return (
                f"{base},"
                f"zoompan=z='1+{self.zoom_strength}*on/{total_frames}':"
                f"d=1:s={self.target_width}x{self.target_height}:fps={self.fps},"
                f"format=yuv420p"
            )

        if animation == "zoom out":
            return (
                f"{base},"
                f"zoompan=z='(1+{self.zoom_strength})-{self.zoom_strength}*on/{total_frames}':"
                f"d=1:s={self.target_width}x{self.target_height}:fps={self.fps},"
                f"format=yuv420p"
            )

        if animation in ("pan left", "pan right"):

            pan_width = int(self.target_width * self.pan_zoom)

            if animation == "pan left":
                x_expr = f"(iw-{self.target_width})*t/{duration}"
            else:
                x_expr = f"(iw-{self.target_width})*(1-t/{duration})"

            return (
                f"scale=w='if(gt(iw/ih,{self.target_width}/{self.target_height}),"
                f"trunc(oh*a/2)*2,{self.target_width})':"
                f"h='if(gt(iw/ih,{self.target_width}/{self.target_height}),"
                f"{self.target_height},trunc(ow/a/2)*2)',"
                f"scale=w='max(iw,{pan_width})':h='max(ih,{self.target_height})',"
                f"crop={self.target_width}:{self.target_height}:x='{x_expr}':y=0,"
                f"fps={self.fps},format=yuv420p"
            )

        return (
            f"{base},"
            f"fps={self.fps},format=yuv420p"
        )

    def _encode_args(self, fast_intermediate=True):

        codec = self.hw_encoder["codec"]

        if self.hw_encoder["type"] == "qsv":
            return [
                "-c:v", codec,
                "-preset", "veryfast",
                "-global_quality", "23",
            ]

        if self.hw_encoder["type"] == "vaapi":
            return [
                "-vaapi_device", self.hw_encoder["device"],
                "-c:v", codec,
                "-qp", "23",
            ]

        preset = "ultrafast" if fast_intermediate else "veryfast"

        return [
            "-c:v", codec,
            "-preset", preset,
            "-crf", "23",
            "-threads", str(self.cpu_count),
        ]

    def _preprocess_scene_video(self, video_path, duration, animation):

        cache_path = self._cache_key(video_path, duration, animation)

        if os.path.exists(cache_path) and os.path.getsize(cache_path) > 0:
            return cache_path

        video_filter = self._build_scene_filter(animation, duration)

        vaapi_pre_input = self.hw_encoder["type"] == "vaapi"

        if vaapi_pre_input:
            cmd = [
                self.ffmpeg_bin, "-y",
                "-vaapi_device", self.hw_encoder["device"],
                "-stream_loop", "-1",
                "-i", video_path,
                "-t", f"{duration:.3f}",
                "-vf", video_filter + ",format=nv12,hwupload",
                "-an",
            ]
        else:
            cmd = [
                self.ffmpeg_bin, "-y",
                "-stream_loop", "-1",
                "-i", video_path,
                "-t", f"{duration:.3f}",
                "-vf", video_filter,
                "-an",
            ]

        cmd += self._encode_args(fast_intermediate=True)

        tmp_path = cache_path + f".tmp.{os.getpid()}.mp4"
        cmd.append(tmp_path)

        result = subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )

        if result.returncode != 0 or not os.path.exists(tmp_path):

            fallback_cmd = [
                self.ffmpeg_bin, "-y",
                "-stream_loop", "-1",
                "-i", video_path,
                "-t", f"{duration:.3f}",
                "-vf", video_filter,
                "-an",
                "-c:v", "libx264",
                "-preset", "ultrafast",
                "-crf", "23",
                "-threads", str(self.cpu_count),
                tmp_path,
            ]

            result = subprocess.run(
                fallback_cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
            )

            if result.returncode != 0:
                raise RuntimeError(
                    f"FFmpeg preprocessing failed for '{video_path}': "
                    f"{result.stderr.decode(errors='ignore')[-800:]}"
                )

        os.replace(tmp_path, cache_path)

        return cache_path

    # ===================================================
    # ZOOM / PAN (legacy Python path for no-scenes fallback)
    # ===================================================

    def _apply_zoom(self, clip, mode):

        duration = clip.duration

        if not duration or duration <= 0:
            return clip

        strength = self.zoom_strength

        if mode == "in":
            def scale(t):
                progress = min(t / duration, 1.0)
                return 1.0 + strength * progress
        else:
            def scale(t):
                progress = min(t / duration, 1.0)
                return (1.0 + strength) - strength * progress

        zoomed = clip.resized(scale)
        zoomed = zoomed.with_position("center")

        return CompositeVideoClip(
            [zoomed],
            size=(self.target_width, self.target_height),
        ).with_duration(duration)

    def _apply_pan(self, clip, direction):

        duration = clip.duration

        if not duration or duration <= 0:
            return clip

        pan_width = int(self.target_width * self.pan_zoom)

        source = clip.resized(height=self.target_height)

        if source.w < pan_width:
            source = source.resized(width=pan_width)

        source = source.cropped(
            y_center=source.h / 2,
            height=self.target_height,
        )

        max_shift = max(source.w - self.target_width, 0)

        def position(t):
            progress = min(t / duration, 1.0)
            if direction == "left":
                x = -max_shift * progress
            else:
                x = -max_shift * (1.0 - progress)
            return (x, "center")

        positioned = source.with_position(position)

        return CompositeVideoClip(
            [positioned],
            size=(self.target_width, self.target_height),
        ).with_duration(duration)

    def apply_animation(self, clip, animation):

        animation = (animation or "").strip().lower()

        if animation == "zoom in":
            return self._apply_zoom(clip, "in")

        if animation == "zoom out":
            return self._apply_zoom(clip, "out")

        if animation == "pan left":
            return self._apply_pan(clip, "left")

        if animation == "pan right":
            return self._apply_pan(clip, "right")

        return clip

    # ===================================================
    # TEXT CLIP CACHE (per compose() call)
    # ===================================================

    def _get_cached_text_clip(self, key, builder):

        cached = self._text_clip_cache.get(key)

        if cached is not None:
            return cached.copy()

        clip = builder()
        self._text_clip_cache[key] = clip

        return clip.copy()

    # ===================================================
    # WHISPER-SYNCED SUBTITLE (BOTTOM BAND)
    # ===================================================

    def caption_clip(
        self,
        text,
        start,
        end,
        width
    ):

        key = (
            "subtitle",
            text,
            self.font_size,
            self.color,
            self.stroke_color,
            self.stroke_width,
            width,
        )

        def builder():
            return TextClip(
                text=text,
                font=self.font,
                font_size=self.font_size,
                color=self.color,
                stroke_color=self.stroke_color,
                stroke_width=self.stroke_width,
                method="caption",
                size=(width - 80, None),
            )

        clip = self._get_cached_text_clip(key, builder)

        clip = clip.with_start(start)
        clip = clip.with_end(end)
        clip = clip.with_position(("center", "bottom"))

        return clip

    def create_subtitles(
        self,
        segments,
        width
    ):

        subtitles = []

        sorted_segments = sorted(
            segments,
            key=lambda item: float(item.get("start", 0.0))
        )

        previous_end = 0.0

        for segment in sorted_segments:

            text = str(segment.get("text", "")).strip()

            if not text:
                continue

            start = float(segment.get("start", 0.0))
            end = float(segment.get("end", start + 1.0))

            if start < previous_end:
                start = previous_end

            if end <= start:
                continue

            clip = self.caption_clip(
                text=text,
                start=start,
                end=end,
                width=width
            )

            subtitles.append(clip)
            previous_end = end

        return subtitles

    # ===================================================
    # SCENE KEYWORD CAPTION (BIG ANIMATED TEXT)
    # ===================================================

    def scene_caption_clip(self, text, start, end):

        duration = max(end - start, 0.1)

        key = (
            "caption",
            text,
            self.caption_font_size,
            self.caption_color,
            self.caption_stroke_color,
            self.caption_stroke_width,
        )

        def builder():
            return TextClip(
                text=text,
                font=self.font,
                font_size=self.caption_font_size,
                color=self.caption_color,
                stroke_color=self.caption_stroke_color,
                stroke_width=self.caption_stroke_width,
                method="caption",
                size=(self.target_width - 140, None),
                text_align="center",
            )

        base_clip = self._get_cached_text_clip(key, builder)

        clip = base_clip.with_duration(duration)

        pop_duration = min(self.caption_pop_duration, duration / 2)

        def scale(t):
            if pop_duration <= 0 or t >= pop_duration:
                return 1.0
            progress = t / pop_duration
            return 0.55 + 0.45 * progress

        clip = clip.resized(scale)

        fade_out_duration = min(0.3, duration / 3) if duration > 0 else 0.0

        effects = []

        if pop_duration > 0:
            effects.append(vfx.FadeIn(pop_duration))

        if fade_out_duration > 0:
            effects.append(vfx.FadeOut(fade_out_duration))

        if effects:
            clip = clip.with_effects(effects)

        clip = clip.with_position(("center", int(self.target_height * 0.18)))
        clip = clip.with_start(start)
        clip = clip.with_end(end)

        return clip

    # ===================================================
    # COMBINE SCENE CLIPS WITH FADE TRANSITIONS
    # ===================================================

    def combine_scenes(self, scene_clips, transitions):

        if not scene_clips:
            raise ValueError("No scene clips to combine")

        if len(scene_clips) == 1:
            single = scene_clips[0].with_start(0)
            return CompositeVideoClip(
                [single],
                size=(self.target_width, self.target_height),
            ).with_duration(single.duration)

        positioned = []
        cursor = 0.0

        for index, clip in enumerate(scene_clips):

            wants_fade = (
                index > 0
                and (transitions[index] or "").strip().lower() == "fade"
            )

            overlap = self.crossfade_duration if wants_fade else 0.0
            overlap = min(overlap, clip.duration / 2)

            start_time = max(cursor - overlap, 0.0)

            positioned_clip = clip.with_start(start_time)

            if wants_fade and overlap > 0:
                positioned_clip = positioned_clip.with_effects(
                    [vfx.CrossFadeIn(overlap)]
                )

            positioned.append(positioned_clip)

            cursor = start_time + clip.duration

        total_duration = max(clip.end for clip in positioned)

        combined = CompositeVideoClip(
            positioned,
            size=(self.target_width, self.target_height),
        ).with_duration(total_duration)

        return combined

    # ===================================================
    # LOAD PREPROCESSED SCENE VIDEO WITH SAFE FALLBACK
    # ===================================================

    def _load_scene_with_fallback(
        self,
        video_path,
        fallback_videos,
        duration,
        animation,
        index,
        opened_resources,
    ):

        candidates = [video_path] if video_path else []
        candidates += list(fallback_videos or [])

        last_error = None

        for candidate in candidates:

            if not candidate:
                continue

            try:
                processed_path = self._preprocess_scene_video(
                    candidate,
                    duration,
                    animation,
                )
                clip = self.load_video(processed_path)

                if clip.duration and clip.duration > 0:
                    opened_resources.append(clip)
                    return clip

                clip.close()

            except Exception as error:
                last_error = error
                print(
                    f"⚠️ Scene {index + 1}: could not preprocess "
                    f"'{candidate}' ({error})"
                )

        raise ValueError(
            f"Scene {index + 1}: no usable video asset found "
            f"(tried '{video_path}' and fallback list). "
            f"Last error: {last_error}"
        )

    # ===================================================
    # BUILD FULL SCENE-WISE COMPOSED VIDEO
    # ===================================================

    def _compose_from_scenes(self, scenes, fallback_videos, timings, opened_resources):

        fallback_videos = fallback_videos or []

        scene_clips = []
        transitions = []

        for index, scene in enumerate(scenes):

            duration = timings[index]["duration"]
            animation = scene.get("animation")
            video_path = scene.get("video")

            clip = self._load_scene_with_fallback(
                video_path,
                fallback_videos,
                duration,
                animation,
                index,
                opened_resources,
            )

            fitted = clip.subclipped(0, min(clip.duration, duration))
            fitted = fitted.with_duration(duration)

            scene_clips.append(fitted)
            transitions.append(scene.get("transition"))

        combined = self.combine_scenes(scene_clips, transitions)

        return combined

    # ===================================================
    # BUILD BIG KEYWORD CAPTIONS PER SCENE
    # ===================================================

    def _build_scene_captions(self, scenes, timings, total_duration):

        clips = []

        for index, scene in enumerate(scenes):

            text = str(scene.get("caption", "")).strip()

            if not text:
                continue

            timing = timings[index]

            start = max(
                timing["start"] - (self.crossfade_duration if index > 0 else 0.0),
                0.0,
            )
            end = min(timing["end"], total_duration)

            if end <= start:
                continue

            clip = self.scene_caption_clip(
                text=text,
                start=start,
                end=end,
            )

            clips.append(clip)

        return clips

    # ===================================================
    # LEGACY FALLBACK: LOAD VIDEOS WITHOUT SCENE JSON
    # ===================================================

    def prepare_videos(
        self,
        videos,
        target_duration
    ):

        clips = []
        total = 0
        index = 0

        while total < target_duration:

            path = videos[index % len(videos)]
            clip = self.load_video(path)
            clip = self.resize_to_target(clip)
            clips.append(clip)
            total += clip.duration
            index += 1

        final = concatenate_videoclips(clips, method="compose")
        final = final.subclipped(0, target_duration)

        return final

    # ===================================================
    # ADD AUDIO (kept for backward compatibility)
    # ===================================================

    def add_audio(self, video, audio):

        audio_clip = self.load_audio(audio)

        duration = min(video.duration, audio_clip.duration)

        video = video.subclipped(0, duration)
        audio_clip = audio_clip.subclipped(0, duration)
        video = video.with_audio(audio_clip)

        return video

    # ===================================================
    # BUILD FINAL AUDIO
    # ===================================================

    def _build_final_audio(
        self,
        voice_audio,
        background_music,
        video_duration,
        opened_resources
    ):

        voice = voice_audio.subclipped(
            0,
            min(voice_audio.duration, video_duration)
        )

        if voice.duration < video_duration - self.sync_tolerance:
            if voice.duration > 0:
                voice = voice.with_effects(
                    [afx.AudioLoop(duration=video_duration)]
                )

        if not background_music:
            return voice.with_duration(video_duration)

        try:
            music = self.load_audio(background_music)
            opened_resources.append(music)
        except Exception as error:
            print(f"⚠️ Background music could not be loaded: {error}")
            return voice.with_duration(video_duration)

        music = music.with_effects([afx.AudioLoop(duration=video_duration)])
        music = music.subclipped(0, video_duration)
        music = music.with_effects([afx.MultiplyVolume(0.18)])

        mixed = CompositeAudioClip([music, voice])
        mixed = mixed.with_duration(video_duration)

        return mixed

    # ===================================================
    # GUARANTEE VIDEO LENGTH == AUDIO LENGTH
    # ===================================================

    def _sync_video_to_audio(self, video, total_duration):

        if video.duration > total_duration + self.sync_tolerance:
            return video.subclipped(0, total_duration)

        if video.duration < total_duration - self.sync_tolerance:
            freeze_point = max(video.duration - 0.001, 0)
            return video.with_effects(
                [vfx.Freeze(t=freeze_point, total_duration=total_duration)]
            )

        return video.with_duration(total_duration)

    # ===================================================
    # POST-RENDER VALIDATION
    # ===================================================

    def _validate_output(self, output):

        probe_cmd = [
            self.ffprobe_bin,
            "-v", "error",
            "-show_entries", "stream=codec_type",
            "-of", "csv=p=0",
            output,
        ]

        try:
            result = subprocess.run(
                probe_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=20,
            )
        except Exception as error:
            print(f"⚠️ Could not validate output with ffprobe: {error}")
            return

        stream_types = result.stdout.decode(errors="ignore").split()

        if "video" not in stream_types:
            raise RuntimeError(
                f"Rendering validation failed: '{output}' has no video stream."
            )

        if "audio" not in stream_types:
            raise RuntimeError(
                f"Rendering validation failed: '{output}' has no audio stream "
                f"(voice is missing from the final render)."
            )

    # ===================================================
    # CREATE FINAL VIDEO
    # ===================================================

    def compose(
        self,
        videos,
        audio,
        subtitle,
        output,
        scenes=None,
        background_music=None,
    ):

        print("=" * 80)
        print("Preparing Video")
        print(
            f"Encoder selected: "
            f"{self.hw_encoder['codec']} ({self.hw_encoder['type']})"
        )
        print("=" * 80)

        started_at = time.time()
        opened_resources = []
        self._text_clip_cache = {}

        try:

            audio_clip = self.load_audio(audio)
            opened_resources.append(audio_clip)

            if not audio_clip.duration or audio_clip.duration <= 0:
                raise ValueError(
                    f"Voice audio '{audio}' has invalid duration"
                )

            total_duration = audio_clip.duration

            if scenes:

                timings = self._compute_scene_timings(scenes, total_duration)

                video = self._compose_from_scenes(
                    scenes=scenes,
                    fallback_videos=videos,
                    timings=timings,
                    opened_resources=opened_resources,
                )

                caption_clips = self._build_scene_captions(
                    scenes=scenes,
                    timings=timings,
                    total_duration=total_duration,
                )

            else:

                video = self.prepare_videos(videos, total_duration)
                caption_clips = []

            video = self._sync_video_to_audio(video, total_duration)

            final_audio = self._build_final_audio(
                audio_clip,
                background_music,
                video.duration,
                opened_resources,
            )

            video = video.with_audio(final_audio)

            segments = subtitle.get("segments", []) if subtitle else []

            if not segments:
                print(
                    "⚠️ No subtitle segments provided; "
                    "final video will have no burned-in subtitles."
                )

            subtitle_clips = self.create_subtitles(segments, int(video.w))

            final = CompositeVideoClip(
                [video, *caption_clips, *subtitle_clips],
                size=video.size
            )

            final = final.with_duration(video.duration)

            os.makedirs(
                os.path.dirname(output) or ".",
                exist_ok=True
            )

            print("=" * 80)
            print("Rendering Started")
            print("=" * 80)

            write_kwargs = dict(
                codec=self.hw_encoder["codec"],
                audio_codec="aac",
                audio_fps=44100,
                audio_bitrate="128k",
                fps=self.fps,
                threads=self.cpu_count,
                ffmpeg_params=[
                    "-pix_fmt", "yuv420p",
                    "-movflags", "+faststart"
                ],
            )

            if self.hw_encoder["type"] == "software":
                write_kwargs["preset"] = "veryfast"
                write_kwargs["ffmpeg_params"] += ["-crf", "23"]

            elif self.hw_encoder["type"] == "qsv":
                write_kwargs["preset"] = "veryfast"
                write_kwargs["ffmpeg_params"] += ["-global_quality", "23"]

            elif self.hw_encoder["type"] == "vaapi":
                write_kwargs["ffmpeg_params"] += [
                    "-vaapi_device", self.hw_encoder["device"],
                    "-vf", "format=nv12,hwupload",
                    "-qp", "23",
                ]

            try:
                final.write_videofile(output, **write_kwargs)
            except Exception as error:
                print(
                    f"⚠️ Hardware/preferred encode failed ({error}); "
                    f"retrying with libx264"
                )
                final.write_videofile(
                    output,
                    codec="libx264",
                    audio_codec="aac",
                    audio_fps=44100,
                    audio_bitrate="128k",
                    fps=self.fps,
                    preset="veryfast",
                    threads=self.cpu_count,
                    ffmpeg_params=[
                        "-pix_fmt", "yuv420p",
                        "-movflags", "+faststart",
                        "-crf", "23"
                    ],
                )

            final.close()
            video.close()

            self._validate_output(output)

            elapsed = time.time() - started_at

            print("=" * 80)
            print(f"Rendering Finished in {elapsed:.1f}s")
            print("=" * 80)

            return output

        finally:

            for resource in opened_resources:
                try:
                    resource.close()
                except Exception:
                    pass