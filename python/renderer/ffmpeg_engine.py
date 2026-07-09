import os
import subprocess

from moviepy import AudioFileClip

from python.renderer.transition_engine import TransitionEngine


class FFmpegEngine:

    def render(

        self,

        audio,

        subtitle,

        videos,

        output

    ):

        print("=" * 60)
        print("Renderer Started")
        print("=" * 60)

        audio_clip = AudioFileClip(audio)

        total_duration = audio_clip.duration

        temp_video = output.replace(

            ".mp4",

            "_timeline.mp4"

        )

        timeline = TransitionEngine()

        timeline.build(

            videos,

            total_duration,

            temp_video

        )

        cmd = [

            "ffmpeg",

            "-y",

            "-i",

            temp_video,

            "-i",

            audio,

            "-map",

            "0:v",

            "-map",

            "1:a",

            "-c:v",

            "copy",

            "-c:a",

            "aac",

            "-shortest",

            output

        ]

        subprocess.run(

            cmd,

            check=True

        )

        if os.path.exists(temp_video):

            os.remove(temp_video)

        print("=" * 60)
        print("Renderer Finished")
        print("=" * 60)

        return output