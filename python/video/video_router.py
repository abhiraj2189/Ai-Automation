from fastapi import APIRouter

from python.video.models import VideoRequest
from python.video.video_service import VideoService

router = APIRouter(

    prefix="/video",

    tags=["Video"]

)


@router.post("/")

def generate(data: VideoRequest):

    service = VideoService()

    return service.generate(

        data.timeline,

        data.voice

    )