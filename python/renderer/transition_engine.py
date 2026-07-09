import os
import subprocess
import tempfile


class TransitionEngine:

    def build(

        self,

        videos,

        total_duration,

        output

    ):

        if not videos:
            raise Exception("No videos found.")

        duration = total_duration / len(videos)

        with tempfile.NamedTemporaryFile(

            mode="w",

            delete=False,

            suffix=".txt"

        ) as file:

            for video in videos:

                file.write(

                    f"file '{os.path.abspath(video)}'\n"

                )

                file.write(

                    f"duration {duration}\n"

                )

            list_file = file.name

        cmd = [

            "ffmpeg",

            "-y",

            "-f",

            "concat",

            "-safe",

            "0",

            "-i",

            list_file,

            "-vf",

            "scale=1080:1920,fps=30",

            "-c:v",

            "libx264",

            output

        ]

        subprocess.run(

            cmd,

            check=True

        )

        os.remove(list_file)

        return output