from python.utils.ollama_client import generate_json
from python.director.prompt_builder import PromptBuilder


SYSTEM = """
You are an expert YouTube Shorts Director.

Return ONLY valid JSON.
"""


class DirectorService:

    def generate(self, script):

        prompt = PromptBuilder.build(script)

        return generate_json(
            prompt=prompt,
            system=SYSTEM
        )