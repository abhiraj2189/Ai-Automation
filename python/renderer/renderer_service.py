import time

from python.renderer.ffmpeg_engine import FFmpegEngine


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

        result = engine.render(

            audio=audio,

            subtitle=subtitle,

            videos=videos,

            output=output

        )

        end = time.time()

        return {

            "status": "completed",

            "output": result,

            "render_time": round(end - start, 2)

        }