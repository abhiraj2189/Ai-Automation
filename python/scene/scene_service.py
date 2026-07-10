from python.scene.prompt_builder import PromptBuilder
from python.utils.ollama_client import generate_json


SYSTEM_PROMPT = """
You are an AI Storyboard Director.

Return ONLY valid JSON.

Every field must be filled.

No markdown.

No explanation.
"""


class SceneService:

    def generate_scene(self, script: str):

        print("=" * 80)
        print("SCRIPT LENGTH :", len(script))
        print(script[:500])
        print("=" * 80)

        prompt = PromptBuilder.build(script)

        print("PROMPT LENGTH :", len(prompt))

        return generate_json(
            prompt=prompt,
            system=SYSTEM_PROMPT
        )