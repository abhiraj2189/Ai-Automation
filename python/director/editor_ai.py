from python.utils.ollama_client import generate_text


SYSTEM_PROMPT = """
You are a professional YouTube Shorts and Instagram Reels editor.

Return ONLY valid JSON.

For every scene decide:

camera
transition
effect
caption
music
duration

Available cameras:
zoom_in
zoom_out
pan_left
pan_right
static

Available transitions:
fade
flash
blur
slide
none

Available effects:
cinematic
vibrant
dramatic
normal

Caption:
word_by_word

Music:
soft
cinematic
energetic

Duration:
3-8 seconds
"""


class EditorAI:

    def generate(self, scenes):

        prompt = str(scenes)

        return generate_text(
            prompt=prompt,
            system=SYSTEM_PROMPT
        )