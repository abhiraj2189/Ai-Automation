from fastapi import APIRouter

from python.projects.project_schema import ProjectCreate
from python.projects.project_service import ProjectService

router = APIRouter(

    prefix="/projects",

    tags=["Projects"]

)


@router.post("/")
def save_project(data: ProjectCreate):

    service = ProjectService()

    return service.save(data)