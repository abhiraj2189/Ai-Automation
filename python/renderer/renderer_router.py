from fastapi import APIRouter

from python.renderer.models import RendererRequest

from python.renderer.renderer_service import RendererService


router = APIRouter(

    prefix="/renderer",

    tags=["Renderer V2"]

)


@router.post("/")

def render(

    data: RendererRequest

):

    service = RendererService()

    return service.render(

        audio=data.audio,

        subtitle=data.subtitle,

        videos=data.videos,

        output=data.output

    )