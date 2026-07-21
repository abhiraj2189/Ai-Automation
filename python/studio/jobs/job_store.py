import uuid


class JobStore:

    jobs = {}

    @classmethod
    def create(cls):

        job_id = str(uuid.uuid4())[:8]

        cls.jobs[job_id] = {

            "progress":0,

            "status":"Starting",

            "video":None,

            "error":None

        }

        return job_id

    @classmethod
    def get(cls, job_id):

        return cls.jobs.get(job_id)