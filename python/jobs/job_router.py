from fastapi import APIRouter

from python.jobs.job_service import JobService


router = APIRouter(

    prefix="/jobs",

    tags=["Jobs"]

)


@router.post("/")

def create():

    service = JobService()

    return service.create()


@router.get("/{job_id}")

def status(job_id: str):

    service = JobService()

    return service.status(job_id)