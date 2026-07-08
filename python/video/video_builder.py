from python.video.audio_mixer import AudioMixer
from python.video.effect_renderer import EffectRenderer
from python.video.transition_renderer import TransitionRenderer


class VideoBuilder:

    def build(

        self,

        timeline,

        voice

    ):

        mixer = AudioMixer()

        effects = EffectRenderer()

        transitions = TransitionRenderer()

        audio = mixer.mix(voice)

        clips = effects.render(timeline)

        clips = transitions.render(clips)

        return {

            "clips": clips,

            "audio": audio

        }