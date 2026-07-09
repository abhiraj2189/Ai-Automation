from fastapi import APIRouter

from python.renderer.models import RenderRequest

from python.renderer.renderer_service import RendererService

router = APIRouter(

    prefix="/render",

    tags=["Renderer"]

)


@router.post("/")

def render(data: RenderRequest):

    service = RendererService()

    return {

        "video": service.render(

            data.video_paths,

            data.audio_path,

            data.subtitle_path,

            data.output

        )

    }