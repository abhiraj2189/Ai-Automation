import subprocess
from pathlib import Path

from python.voice.voice_engine import VoiceEngine
from python.config.settings import settings


class PiperEngine(VoiceEngine):

    def generate(
        self,
        text: str,
        language: str,
        output_path: str
    ) -> str:

        # Language Model Select

        if language == "hindi":
            model = settings.HINDI_MODEL

        elif language == "hinglish":
            model = settings.HINGLISH_MODEL

        else:
            model = settings.ENGLISH_MODEL

        Path(output_path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        command = [
            settings.PIPER_PATH,
            "-m",
            model,
            "-f",
            output_path
        ]

        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            text=True
        )

        process.communicate(text)

        return output_path