import shutil
import subprocess


class FFmpegUtils:

    @staticmethod
    def exists():

        return shutil.which("ffmpeg") is not None

    @staticmethod
    def ffprobe_exists():

        return shutil.which("ffprobe") is not None

    @staticmethod
    def version():

        if not FFmpegUtils.exists():
            return None

        result = subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            text=True
        )

        return result.stdout.split("\n")[0]

    @staticmethod
    def video_info(video):

        if not FFmpegUtils.ffprobe_exists():
            return {}

        cmd = [
            "ffprobe",
            "-v",
            "quiet",
            "-print_format",
            "json",
            "-show_streams",
            video
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        return result.stdout

    @staticmethod
    def default_encode():

        return {
            "codec": "libx264",
            "preset": "veryfast",
            "audio_codec": "aac",
            "fps": 24,
            "threads": 4,
            "bitrate": "2500k"
        }