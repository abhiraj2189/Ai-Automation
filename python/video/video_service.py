from python.video.video_builder import VideoBuilder


class VideoService:

    def generate(

        self,

        timeline,

        voice

    ):

        builder = VideoBuilder()

        return builder.build(

            timeline,

            voice

        )