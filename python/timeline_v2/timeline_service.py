from python.timeline_v2.timeline_engine import TimelineEngine


class TimelineService:

    def generate(

        self,

        scenes,

        videos,

        audio

    ):

        engine = TimelineEngine()

        return engine.generate(

            scenes=scenes,

            videos=videos,

            audio=audio

        )