from fastapi import APIRouter

from python.progress.progress_service import ProgressService

router = APIRouter(

    prefix="/progress",

    tags=["Progress"]

)


@router.get("/{job_id}")

def progress(job_id: str):

    service = ProgressService()

    return service.status(job_id)