import json
import time

from concurrent.futures import ThreadPoolExecutor, as_completed

from python.jobs.job_manager import JobManager

from python.research.research_service import ResearchService
from python.script.script_service import ScriptService
from python.scene.scene_service import SceneService
from python.voice.voice_service import VoiceService
from python.subtitles.subtitle_service import SubtitleService
from python.assets.asset_service import AssetService
from python.composer.composer_service import ComposerService

from python.config.settings import settings


class WorkflowService:

    # How many scene-wise asset downloads run at the same time.
    # Kept modest to avoid hammering the Pexels API / hitting
    # rate limits when there are many scenes.
    MAX_PARALLEL_DOWNLOADS = 6

    # ===================================================
    # SCENE JSON NORMALIZATION
    # SceneService may return a Python list already, or (in some
    # setups) a raw JSON string. Handle both without assuming
    # which one, so we never crash on a perfectly valid response.
    # ===================================================

    def _normalize_scenes(self, scenes):

        if isinstance(scenes, str):
            try:
                scenes = json.loads(scenes)
            except (ValueError, TypeError):
                scenes = []

        if not isinstance(scenes, list):
            scenes = []

        normalized = []

        for scene in scenes:
            if isinstance(scene, dict):
                normalized.append(dict(scene))

        return normalized

    # ===================================================
    # GLOBAL ASSET DOWNLOAD (unchanged behaviour/signature,
    # just extracted into its own method so it can be run on
    # a worker thread in parallel with Voice generation)
    # ===================================================

    def _download_global_assets(self, topic):

        return AssetService().download(
            keyword=topic,
            count=2
        )

    # ===================================================
    # SINGLE SCENE ASSET DOWNLOAD (one Pexels call per scene,
    # designed to be fired concurrently from a thread pool)
    # ===================================================

    def _download_scene_asset(self, index, scene, topic):

        keyword = scene.get("visual") or topic

        try:
            scene_assets = AssetService().download(
                keyword=keyword,
                count=1
            )
            if scene_assets:
                return index, scene_assets[0].get("path")
        except Exception as error:
            print(
                f"⚠️ Scene {index + 1} asset fetch failed "
                f"for '{keyword}': {error}"
            )

        return index, None

    # ===================================================
    # PARALLEL PER-SCENE ASSET DOWNLOAD
    # Every scene's dedicated video is fetched concurrently
    # instead of one-by-one, then falls back to the round-robin
    # global asset pool for any scene that failed to fetch.
    # ===================================================

    def _prepare_scene_assets_parallel(self, scenes, topic, fallback_videos):

        prepared = [dict(scene) for scene in scenes]

        if not scenes:
            return prepared

        worker_count = min(self.MAX_PARALLEL_DOWNLOADS, len(scenes))

        with ThreadPoolExecutor(max_workers=worker_count) as executor:

            futures = [
                executor.submit(self._download_scene_asset, index, scene, topic)
                for index, scene in enumerate(scenes)
            ]

            for future in as_completed(futures):

                index, video_path = future.result()

                if not video_path and fallback_videos:
                    video_path = fallback_videos[index % len(fallback_videos)]

                prepared[index]["video"] = video_path

        return prepared

    # ===================================================
    # FULL ASSETS STAGE (global pool + scene-wise, parallel)
    # Runs entirely on a worker thread so it can overlap with
    # Voice + Subtitle generation, since assets only depend on
    # topic/scenes, never on voice or subtitle output.
    # ===================================================

    def _run_assets_stage(self, topic, normalized_scenes):

        assets = self._download_global_assets(topic)

        videos = [
            item["path"]
            for item in assets
        ]

        prepared_scenes = self._prepare_scene_assets_parallel(
            normalized_scenes,
            topic,
            videos
        )

        return assets, videos, prepared_scenes

    # ===================================================
    # VOICE + SUBTITLE STAGE
    # Subtitle depends on the finished voice file, so these two
    # stay sequential relative to each other, but the whole
    # stage runs in parallel with the Assets stage above.
    # ===================================================

    def _run_voice_and_subtitle_stage(self, script, job_id):

        if job_id:
            JobManager.update(job_id, 55, "Generating Voice")

        voice_path = "outputs/audio/voice.wav"

        VoiceService().generate(
            text=script,
            output=voice_path,
            language="hinglish_male"
        )

        voice = {
            "audio": voice_path
        }

        if job_id:
            JobManager.update(job_id, 65, "Generating Subtitle")

        subtitle = SubtitleService().generate(
            voice["audio"]
        )

        return voice, subtitle

    # ===================================================
    # MAIN WORKFLOW
    # ===================================================

    def run(self, topic: str, job_id: str = None):

        workflow_started_at = time.time()

        try:

            print("\n==============================")
            print("🚀 AI AUTOMATION WORKFLOW START")
            print("TOPIC :", topic)
            print("==============================\n")

            # ======================================
            # RESEARCH
            # ======================================

            step_started_at = time.time()

            print("🔎 STEP 1 : Research")

            if job_id:
                JobManager.update(job_id, 10, "Generating Research")

            research = ResearchService().generate_research(topic)

            print(f"✅ Research Completed ({time.time() - step_started_at:.1f}s)")

            # ======================================
            # SCRIPT
            # ======================================

            step_started_at = time.time()

            print("\n📝 STEP 2 : Script")

            if job_id:
                JobManager.update(job_id, 25, "Generating Script")

            script = ScriptService().generate_script(research)

            script = script.replace(
                "[TELEGRAM_LINK]",
                settings.TELEGRAM_LINK
            )

            print(f"✅ Script Completed ({time.time() - step_started_at:.1f}s)")

            # ======================================
            # SCENE
            # ======================================

            step_started_at = time.time()

            print("\n🎬 STEP 3 : Scene")

            if job_id:
                JobManager.update(job_id, 40, "Generating Scene")

            scenes = SceneService().generate_scene(script)

            normalized_scenes = self._normalize_scenes(scenes)

            print(f"✅ Scene Completed ({time.time() - step_started_at:.1f}s)")

            # ======================================
            # VOICE + SUBTITLE  <-- runs in parallel with -->  ASSETS
            #
            # Assets only need 'topic' / 'scenes', which are
            # already available at this point -- there is no
            # reason to wait for Voice/Subtitle to finish before
            # starting downloads. This is the single biggest
            # workflow-level time saver, since Assets and Voice
            # were previously fully sequential despite having no
            # real dependency on each other.
            # ======================================

            step_started_at = time.time()

            print("\n🎤 STEP 4 : Voice + Subtitle   🖼 STEP 4 : Assets   (parallel)")

            if job_id:
                JobManager.update(job_id, 55, "Generating Voice & Downloading Assets")

            with ThreadPoolExecutor(max_workers=2) as executor:

                voice_subtitle_future = executor.submit(
                    self._run_voice_and_subtitle_stage,
                    script,
                    job_id
                )

                assets_future = executor.submit(
                    self._run_assets_stage,
                    topic,
                    normalized_scenes
                )

                voice, subtitle = voice_subtitle_future.result()
                assets, videos, prepared_scenes = assets_future.result()

            print(
                f"✅ Voice + Subtitle + Assets Completed "
                f"({time.time() - step_started_at:.1f}s)"
            )

            # ======================================
            # COMPOSER
            # ======================================

            step_started_at = time.time()

            print("\n🎥 STEP 5 : Composer")

            if job_id:
                JobManager.update(job_id, 95, "Rendering Video")

            result = ComposerService().generate(
                audio=voice["audio"],
                subtitle=subtitle,
                videos=videos,
                output="outputs/final/final_video.mp4",
                scenes=prepared_scenes
            )

            print(f"✅ Composer Completed ({time.time() - step_started_at:.1f}s)")

            if job_id:
                JobManager.complete(
                    job_id,
                    result["video"]
                )

            total_elapsed = time.time() - workflow_started_at

            print(f"\n🎉 AI VIDEO GENERATED SUCCESSFULLY in {total_elapsed:.1f}s")

            return {
                "topic": topic,
                "research": research,
                "script": script,
                "scenes": scenes,
                "voice": voice,
                "subtitle": subtitle,
                "assets": assets,
                "video": result["video"]
            }

        except Exception as e:

            print("\n❌ WORKFLOW FAILED")
            print(type(e).__name__)
            print(str(e))

            if job_id:
                JobManager.failed(
                    job_id,
                    str(e)
                )

            raise