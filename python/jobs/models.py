from enum import Enum
from typing import Optional

from pydantic import BaseModel


class JobStatus(str, Enum):

    PENDING = "Pending"

    RUNNING = "Running"

    COMPLETED = "Completed"

    FAILED = "Failed"


class JobRequest(BaseModel):

    topic: str


class JobResponse(BaseModel):

    job_id: str

    status: JobStatus


class JobProgress(BaseModel):

    job_id: str

    topic: str

    status: JobStatus

    progress: int = 0

    current_step: str = "Waiting"

    output: Optional[str] = None

    error: Optional[str] = None