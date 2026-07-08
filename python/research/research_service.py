from python.research.prompt_builder import PromptBuilder
from python.utils.ollama_client import generate_text


SYSTEM_PROMPT = """
You are a senior technical researcher.

Never invent facts.

If unsure, omit the fact.

Never guess version numbers.

Never guess statistics.

Return only the research.
"""


class ResearchService:

    def generate_research(self, topic: str):

        prompt = PromptBuilder.build(topic)

        return generate_text(
            prompt=prompt,
            system=SYSTEM_PROMPT
        )