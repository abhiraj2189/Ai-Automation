from fastapi import APIRouter

from python.timeline_v2.models import TimelineRequest

from python.timeline_v2.timeline_service import TimelineService


router = APIRouter(

    prefix="/timeline",

    tags=["Timeline"]

)


@router.post("/")

def generate(

    data: TimelineRequest

):

    service = TimelineService()

    return service.generate(

        scenes=data.scenes,

        videos=data.videos,

        audio=data.audio

    )