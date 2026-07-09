from fastapi import APIRouter

from python.director.models import DirectorRequest

from python.director.director_service import DirectorService


router = APIRouter(

    prefix="/director",

    tags=["AI Director"]

)


@router.post("/")

def generate(

    data: DirectorRequest

):

    return DirectorService().generate(

        data.script,

        data.scenes

    )