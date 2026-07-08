from pathlib import Path


class Renderer:

    def render(
        self,
        timeline,
        voice,
        output
    ):

        Path(output).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        print("=" * 60)
        print("AI AUTOMATION VIDEO RENDERER")
        print("=" * 60)

        print("Voice :", voice)

        print("Scenes :", len(timeline))

        print("Output :", output)

        return output