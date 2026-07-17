from python.composer.video_composer import VideoComposer


class ComposerService:

    def __init__(self):
        self.composer = VideoComposer()

    def generate(
        self,
        audio,
        subtitle,
        videos,
        output,
        scenes=None,
        background_music=None
    ):

        result = self.composer.compose(
            audio=audio,
            subtitle=subtitle,
            videos=videos,
            output=output,
            scenes=scenes,
            background_music=background_music
        )

        return {
            "status": "completed",
            "video": result
        }