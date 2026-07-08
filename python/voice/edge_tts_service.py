import asyncio

import edge_tts

from python.voice.voice_selector import VoiceSelector


class EdgeTTSService:

    async def generate(

        self,

        text,

        output,

        language

    ):

        voice = VoiceSelector.get(language)

        communicate = edge_tts.Communicate(

            text,

            voice

        )

        await communicate.save(output)