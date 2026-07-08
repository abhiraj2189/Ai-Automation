from fastapi import APIRouter

from python.director.models import DirectorRequest
from python.director.director_service import DirectorService

router = APIRouter(
    prefix="/director",
    tags=["Director"]
)


@router.post("/")
def generate(data: DirectorRequest):

    service = DirectorService()

    return service.generate(data.script)