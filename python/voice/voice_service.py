import asyncio

from python.voice.edge_tts_service import EdgeTTSService


class VoiceService:

    def generate(

        self,

        text,

        output,

        language="hindi_male"

    ):

        service = EdgeTTSService()

        asyncio.run(

            service.generate(

                text,

                output,

                language

            )

        )

        return output