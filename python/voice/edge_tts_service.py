import os
import edge_tts

from python.voice.voice_selector import VoiceSelector


class EdgeTTSService:

    async def generate(
        self,
        text,
        output,
        language
    ):
        # Create output folder if it doesn't exist
        os.makedirs(os.path.dirname(output), exist_ok=True)

        voice = VoiceSelector.get(language)

        communicate = edge_tts.Communicate(
            text=text,
            voice=voice
        )

        await communicate.save(output)

        return output