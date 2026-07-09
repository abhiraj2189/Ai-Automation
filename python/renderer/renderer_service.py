import os
import time

from python.renderer.ffmpeg_engine import FFmpegEngine
from python.renderer.subtitle_renderer import SubtitleRenderer


class RendererService:

    def render(

        self,

        audio,

        subtitle,

        videos,

        output

    ):

        start = time.time()

        engine = FFmpegEngine()

        temp_video = output.replace(

            ".mp4",

            "_temp.mp4"

        )

        engine.render(

            audio=audio,

            subtitle=None,

            videos=videos,

            output=temp_video

        )

        renderer = SubtitleRenderer()

        renderer.burn(

            temp_video,

            subtitle,

            output

        )

        if os.path.exists(temp_video):

            os.remove(temp_video)

        end = time.time()

        return {

            "status": "completed",

            "video": output,

            "render_time": round(

                end - start,

                2

            )

        }