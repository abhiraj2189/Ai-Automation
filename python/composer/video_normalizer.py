import os
import subprocess


class VideoNormalizer:

    WIDTH = 720
    HEIGHT = 1280
    FPS = 24

    def normalize(
        self,
        input_video: str,
        output_video: str
    ):

        os.makedirs(
            os.path.dirname(output_video),
            exist_ok=True
        )

        command = [

            "ffmpeg",

            "-y",

            "-i",
            input_video,

            "-vf",
            f"scale={self.WIDTH}:{self.HEIGHT}:force_original_aspect_ratio=cover,crop={self.WIDTH}:{self.HEIGHT}",

            "-r",
            str(self.FPS),

            "-c:v",
            "libx264",

            "-preset",
            "veryfast",

            "-pix_fmt",
            "yuv420p",

            "-c:a",
            "aac",

            "-b:a",
            "128k",

            output_video

        ]

        subprocess.run(

            command,

            check=True,

            stdout=subprocess.DEVNULL,

            stderr=subprocess.DEVNULL

        )

        return output_video