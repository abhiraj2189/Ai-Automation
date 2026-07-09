import os

from moviepy import (
    VideoFileClip,
    AudioFileClip,
    concatenate_videoclips
)


class MoviePyEngine:

    def compose(
        self,
        videos,
        audio,
        subtitle,
        output
    ):

        clips = []

        for video in videos:

            if os.path.exists(video):
                clips.append(VideoFileClip(video))

        if not clips:
            raise Exception("No video files found.")

        final = concatenate_videoclips(
            clips,
            method="compose"
        )

        if os.path.exists(audio):

            audio_clip = AudioFileClip(audio)

            final = final.with_audio(audio_clip)

        os.makedirs(
            os.path.dirname(output),
            exist_ok=True
        )

        final.write_videofile(
            output,
            codec="libx264",
            audio_codec="aac",
            fps=30
        )

        return output