import os
import subprocess
import tempfile


class FFmpegEngine:

    def render(
        self,
        audio,
        subtitle,
        videos,
        output
    ):

        if not videos:
            raise Exception("No videos found.")

        os.makedirs(
            os.path.dirname(output),
            exist_ok=True
        )

        # -----------------------
        # Create temp video list
        # -----------------------

        with tempfile.NamedTemporaryFile(
            mode="w",
            delete=False,
            suffix=".txt"
        ) as f:

            for video in videos:

                if os.path.exists(video):
                    f.write(
                        f"file '{os.path.abspath(video)}'\n"
                    )

            list_file = f.name

        merged_video = output.replace(
            ".mp4",
            "_merged.mp4"
        )

        # -----------------------
        # Merge Videos
        # -----------------------

        subprocess.run(

            [
                "ffmpeg",
                "-y",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                list_file,
                "-c",
                "copy",
                merged_video
            ],

            check=True

        )

        # -----------------------
        # Add Audio
        # -----------------------

        subprocess.run(

            [
                "ffmpeg",
                "-y",
                "-i",
                merged_video,
                "-i",
                audio,
                "-c:v",
                "copy",
                "-c:a",
                "aac",
                "-shortest",
                output
            ],

            check=True

        )

        # Cleanup

        os.remove(list_file)

        os.remove(merged_video)

        return output