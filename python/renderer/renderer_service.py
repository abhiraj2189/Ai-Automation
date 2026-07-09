from python.renderer.video_renderer import VideoRenderer
from python.renderer.audio_mixer import AudioMixer
from python.renderer.subtitle_renderer import SubtitleRenderer


class RendererService:

    def render(

        self,

        videos,

        audio,

        subtitle,

        output

    ):

        renderer = VideoRenderer()

        mixer = AudioMixer()

        sub = SubtitleRenderer()

        clip = renderer.render(videos)

        clip = clip.with_audio(

            mixer.load(audio)

        )

        clip = sub.apply(

            clip,

            subtitle

        )

        clip.write_videofile(

            output,

            fps=30,

            codec="libx264",

            audio_codec="aac"

        )

        return output