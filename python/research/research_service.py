import ollama

from python.research.prompt_builder import PromptBuilder


class ResearchService:

    def generate_research(self, topic: str):

        prompt = PromptBuilder.build(topic)

        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]