from python.timeline.timeline_builder import TimelineBuilder


class TimelineService:

    def generate(

        self,

        scenes,

        subtitles,

        voice

    ):

        builder = TimelineBuilder()

        return builder.build(

            scenes,

            subtitles,

            voice

        )