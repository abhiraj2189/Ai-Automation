class PromptBuilder:

    @staticmethod
    def build(script: str):

        # Llama ke liye prompt chhota rakho
        script = script[:1500]

        return f"""
You are an AI storyboard generator.

Return ONLY a valid JSON array.

Do not explain anything.

Do not use markdown.

JSON format:

[
  {{
    "scene": 1,
    "duration": "0-5 sec",
    "voice": "...",
    "visual": "...",
    "caption": "...",
    "animation": "Zoom In",
    "transition": "Fade"
  }}
]

SCRIPT:

{script}
"""