from fastapi import APIRouter

from python.subtitles.models import SubtitleRequest
from python.subtitles.subtitle_service import SubtitleService

router = APIRouter(
    prefix="/subtitles",
    tags=["Subtitles"]
)


@router.post("/")
def generate(data: SubtitleRequest):

    service = SubtitleService()

    return service.generate(data.audio)