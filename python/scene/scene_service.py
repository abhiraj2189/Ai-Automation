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

        prompt = PromptBuilder.build(script)

        try:

            return generate_json(
                prompt=prompt,
                system=SYSTEM_PROMPT
            )

        except ValueError:

            return [
                {
                    "scene": 1,
                    "duration": "0-10 sec",
                    "voice": script[:200],
                    "visual": "Technology",
                    "caption": "AI Automation",
                    "animation": "Zoom In",
                    "transition": "Fade"
                }
            ]