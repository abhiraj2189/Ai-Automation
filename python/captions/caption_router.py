from fastapi import APIRouter

from python.captions.models import CaptionRequest

from python.captions.caption_service import CaptionService


router = APIRouter(

    prefix="/captions",

    tags=["Captions"]

)


@router.post("/")

def generate(data: CaptionRequest):

    service = CaptionService()

    return service.generate(

        data.subtitle_file

    )