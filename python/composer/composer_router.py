from fastapi import APIRouter

from python.composer.models import ComposerRequest

from python.composer.composer_service import ComposerService


router = APIRouter(

    prefix="/composer",

    tags=["Composer"]

)


@router.post("/")

def compose(data: ComposerRequest):

    service = ComposerService()

    return service.generate(

        data.audio,

        data.subtitle,

        data.videos,

        data.output

    )