import uuid

from python.jobs.job_repository import JobRepository


class JobManager:

    repository = JobRepository()

    @classmethod
    def create_job(
        cls,
        topic: str
    ):

        job_id = str(uuid.uuid4())

        cls.repository.create_job(
            job_id,
            topic
        )

        return cls.repository.get_job(
            job_id
        )

    @classmethod
    def get_job(
        cls,
        job_id: str
    ):

        return cls.repository.get_job(
            job_id
        )

    @classmethod
    def update(
        cls,
        job_id,
        progress,
        step
    ):

        job = cls.repository.get_job(
            job_id
        )

        if job is None:
            return

        cls.repository.update(

            job_id=job_id,

            status="Running",

            progress=progress,

            step=step,

            output=job["output"],

            error=job["error"]

        )

    @classmethod
    def complete(
        cls,
        job_id,
        output
    ):

        cls.repository.update(

            job_id=job_id,

            status="Completed",

            progress=100,

            step="Completed",

            output=output,

            error=""

        )

    @classmethod
    def failed(
        cls,
        job_id,
        error
    ):

        cls.repository.update(

            job_id=job_id,

            status="Failed",

            progress=0,

            step="Failed",

            output="",

            error=str(error)

        )