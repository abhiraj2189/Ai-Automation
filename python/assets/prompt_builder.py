class PromptBuilder:

    @staticmethod
    def build(scenes):

        return f"""
You are an AI Video Production Assistant.

Using the following scene JSON:

{scenes}

Generate assets for every scene.

Return ONLY valid JSON.

Format:

[
  {{
    "scene":1,
    "voice_segment":"...",
    "image_prompt":"...",
    "pexels_keyword":"...",
    "music":"Technology",
    "sound_effect":"Whoosh"
  }}
]

Never leave any field empty.
"""