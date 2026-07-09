from python.composer.moviepy_engine import MoviePyEngine


class VideoComposer:

    def compose(
        self,
        audio,
        subtitle,
        videos,
        output
    ):

        engine = MoviePyEngine()

        video = engine.compose(
            videos=videos,
            audio=audio,
            subtitle=subtitle,
            output=output
        )

        return {
            "status": "completed",
            "video": video
        }