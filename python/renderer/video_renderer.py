from moviepy import (
    VideoFileClip,
    concatenate_videoclips,
)


class VideoRenderer:

    def render(self, videos):

        clips = []

        for path in videos:

            clips.append(

                VideoFileClip(path)

            )

        return concatenate_videoclips(
            clips,
            method="compose"
        )