from pydantic import BaseModel


class JobRequest(BaseModel):

    topic: str


class JobResponse(BaseModel):

    job_id: str

    status: str