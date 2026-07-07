from fastapi import APIRouter

from python.studio.studio_service import StudioService
from python.studio.studio_schema import TopicRequest

router = APIRouter(
    prefix="/studio",
    tags=["AI Studio"]
)


@router.post("/")
def generate(data: TopicRequest):

    service = StudioService()

    result = service.generate(data.topic)

    return {
        "success": True,
        "data": result
    }