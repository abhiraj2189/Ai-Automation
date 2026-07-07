import ollama

from python.script.prompt_builder import PromptBuilder


class ScriptService:

    def generate_script(self, research: str):

        prompt = PromptBuilder.build(research)

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