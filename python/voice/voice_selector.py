from python.voice.voice_config import VOICE_MODELS


class VoiceSelector:

    @staticmethod
    def get(language="hindi_male"):

        return VOICE_MODELS.get(

            language,

            VOICE_MODELS["hindi_male"]

        )