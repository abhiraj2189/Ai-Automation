from python.timeline.scene_timeline import SceneTimeline
from python.timeline.audio_timeline import AudioTimeline
from python.timeline.caption_timeline import CaptionTimeline
from python.timeline.transition_timeline import TransitionTimeline


class TimelineBuilder:

    def build(

        self,

        scenes,

        subtitles,

        voice

    ):

        scene = SceneTimeline()

        caption = CaptionTimeline()

        audio = AudioTimeline()

        transition = TransitionTimeline()

        timeline = scene.build(scenes)

        timeline = transition.apply(timeline)

        return {

            "timeline": timeline,

            "captions": caption.build(subtitles),

            "audio": audio.build(voice)

        }