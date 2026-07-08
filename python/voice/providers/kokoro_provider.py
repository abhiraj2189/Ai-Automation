from python.voice.providers.base_provider import BaseVoiceProvider


class KokoroProvider(BaseVoiceProvider):

    def generate(self, text: str, output_path: str):
        raise NotImplementedError(
            "Kokoro provider not configured yet."
        )