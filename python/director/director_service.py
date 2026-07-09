import re


class DirectorService:

    def generate(self, script):

        sentences = re.split(r"[.!?]", script)

        scenes = []

        for i, text in enumerate(sentences):

            text = text.strip()

            if not text:
                continue

            scenes.append({

                "scene": i + 1,

                "text": text,

                "asset": text[:40],

                "duration": 5

            })

        return {

            "scenes": scenes

        }