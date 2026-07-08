from python.assets.prompt_builder import PromptBuilder
from python.utils.ollama_client import generate_json


SYSTEM = """
Return only valid JSON.

Never use markdown.

Every field must be filled.
"""


class AssetService:

    def generate_assets(self, scenes):

        prompt = PromptBuilder.build(scenes)

        return generate_json(
            prompt=prompt,
            system=SYSTEM
        )