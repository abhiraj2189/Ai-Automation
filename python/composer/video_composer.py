from python.composer.moviepy_engine import MoviePyEngine


class VideoComposer:

    def __init__(self):
        self.engine = MoviePyEngine()

    def compose(
        self,
        videos,
        audio,
        subtitle,
        output,
        scenes=None,
        background_music=None
    ):

        return self.engine.compose(
            videos=videos,
            audio=audio,
            subtitle=subtitle,
            output=output,
            scenes=scenes,
            background_music=background_music
        )