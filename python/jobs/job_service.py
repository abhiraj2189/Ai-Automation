from python.jobs.job_manager import JobManager


class JobService:

    def create(self):

        job_id = JobManager.create()

        return {

            "job_id": job_id,

            "status": "pending"

        }

    def status(

        self,

        job_id

    ):

        return JobManager.get(job_id)