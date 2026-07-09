from fastapi import APIRouter
from fastapi import HTTPException

from python.jobs.models import JobRequest
from python.jobs.job_service import JobService


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

service = JobService()


@router.post("/")
def create_job(data: JobRequest):

    return service.create_job(
        topic=data.topic
    )


@router.get("/{job_id}")
def get_job(job_id: str):

    result = service.get_job(job_id)

    if not result["success"]:
        raise HTTPException(
            status_code=404,
            detail=result["message"]
        )

    return result