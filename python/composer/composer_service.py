from python.composer.video_composer import VideoComposer


class ComposerService:

    def generate(
        self,
        audio,
        subtitle,
        videos,
        output
    ):

        composer = VideoComposer()

        return composer.compose(
            audio=audio,
            subtitle=subtitle,
            videos=videos,
            output=output
        )