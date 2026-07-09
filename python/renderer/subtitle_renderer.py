import os
import subprocess


class SubtitleRenderer:

    def burn(

        self,

        video,

        subtitle,

        output

    ):

        if not subtitle:

            return video

        if not os.path.exists(subtitle):

            return video

        print("=" * 60)
        print("Burning Subtitle...")
        print("=" * 60)

        cmd = [

            "ffmpeg",

            "-y",

            "-i",
            video,

            "-vf",
            f"subtitles={subtitle}",

            "-c:a",
            "copy",

            output

        ]

        subprocess.run(

            cmd,

            check=True

        )

        print("Subtitle Added")

        return output