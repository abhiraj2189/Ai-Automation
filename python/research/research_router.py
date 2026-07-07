from fastapi import APIRouter
from pydantic import BaseModel

from python.research.research_service import ResearchService

router = APIRouter(
    prefix="/research",
    tags=["AI Research"]
)


class ResearchRequest(BaseModel):
    topic: str


@router.post("/")
def research(data: ResearchRequest):

    service = ResearchService()

    result = service.generate_research(data.topic)

    return {
        "success": True,
        "topic": data.topic,
        "research": result
    }