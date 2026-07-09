from python.utils.ollama_client import generate_json


SYSTEM_PROMPT = """
You are an AI Asset Planner.

Return ONLY JSON.

For every scene generate one search keyword.

JSON:

[
 {
   "scene":1,
   "keyword":"python programming",
   "asset":"video"
 }
]
"""


class PlannerEngine:

    def generate(

        self,

        scenes

    ):

        prompt = f"""

Scenes:

{scenes}

"""

        return generate_json(

            prompt,

            SYSTEM_PROMPT

        )