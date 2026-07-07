import json
import ollama

from python.scene.prompt_builder import PromptBuilder


class SceneService:

    def generate_scene(self, script: str):

        prompt = PromptBuilder.build(script)

        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response["message"]["content"]

        try:
            return json.loads(content)
        except Exception:
            return [
                {
                    "scene": 1,
                    "duration": "Unknown",
                    "voice": content,
                    "visual": "",
                    "caption": "",
                    "animation": "",
                    "transition": ""
                }
            ]