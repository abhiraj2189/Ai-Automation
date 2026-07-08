from pathlib import Path

from python.voice.providers.kokoro_provider import KokoroProvider


class VoiceService:

    def __init__(self):

        self.provider = KokoroProvider()

    def generate(self, text: str):

        output_dir = Path("python/voice/outputs")
        output_dir.mkdir(parents=True, exist_ok=True)

        output_path = output_dir / "voice.wav"

        self.provider.generate(
            text=text,
            output_path=str(output_path)
        )

        return {
            "audio_path": str(output_path)
        }