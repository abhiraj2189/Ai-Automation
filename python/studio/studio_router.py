from fastapi import APIRouter
from pydantic import BaseModel

from python.studio.studio_service import StudioService


router = APIRouter(

    prefix="/studio",

    tags=["AI Studio"]

)


class StudioRequest(BaseModel):

    topic: str


@router.post("/")

def generate(

    data: StudioRequest

):

    service = StudioService()

    return service.generate(

        topic=data.topic

    )