import os
import whisper


# FFmpeg path (Windows)
FFMPEG_PATH = r"C:\ffmpeg\ffmpeg-8.1.2-essentials_build\bin"

# Add ffmpeg to PATH for current Python process
os.environ["PATH"] = FFMPEG_PATH + os.pathsep + os.environ["PATH"]


class WhisperService:

    def __init__(self):
        self.model = whisper.load_model("base")

    def transcribe(self, audio):
        result = self.model.transcribe(
            audio,
            word_timestamps=True
        )

        return result