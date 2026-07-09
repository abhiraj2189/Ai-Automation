from python.utils.ollama_client import generate_json


SYSTEM_PROMPT = """
You are an AI Film Director.

Return ONLY valid JSON.

For every scene decide:

- keyword
- asset_type
- camera
- transition
- animation
- emotion

Return JSON only.
"""


class DirectorEngine:

    def generate(

        self,

        script,

        scenes

    ):

        prompt = f"""

Script:

{script}

Scenes:

{scenes}

"""

        return generate_json(

            prompt,

            SYSTEM_PROMPT

        )