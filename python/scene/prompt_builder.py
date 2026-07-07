class PromptBuilder:

    @staticmethod
    def build(script: str):

        return f"""
You are an expert AI Video Director.

Convert the following script into a scene-by-scene storyboard.

Return ONLY valid JSON.

Format:

[
  {{
    "scene":1,
    "duration":"0-4 sec",
    "voice":"...",
    "visual":"...",
    "caption":"...",
    "animation":"...",
    "transition":"..."
  }}
]

Script:

{script}
"""