import uuid


class JobManager:

    jobs = {}

    @classmethod
    def create(cls):

        job_id = str(uuid.uuid4())

        cls.jobs[job_id] = {

            "status": "pending"

        }

        return job_id

    @classmethod
    def update(

        cls,

        job_id,

        status

    ):

        cls.jobs[job_id]["status"] = status

    @classmethod
    def get(

        cls,

        job_id

    ):

        return cls.jobs.get(job_id)