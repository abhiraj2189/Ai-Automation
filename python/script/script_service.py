from python.script.prompt_builder import PromptBuilder
from python.utils.ollama_client import generate_text


SYSTEM_PROMPT = """
You are an expert YouTube Shorts script writer.

No greetings.

Never start with:

Hi everyone
Hello everyone
Welcome back

Always start with a curiosity hook or shocking fact.

Return only the script.
"""


class ScriptService:

    def generate_script(self, research: str):

        prompt = PromptBuilder.build(research)

        return generate_text(
            prompt=prompt,
            system=SYSTEM_PROMPT
        )