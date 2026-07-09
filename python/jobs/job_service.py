from python.jobs.job_manager import JobManager
from python.jobs.worker import Worker


class JobService:

    def create_job(
        self,
        topic: str
    ):

        job = JobManager.create_job(topic)

        Worker.start(
            job["job_id"],
            topic
        )

        return {
            "success": True,
            "job_id": job["job_id"],
            "status": job["status"]
        }

    def get_job(
        self,
        job_id: str
    ):

        job = JobManager.get_job(job_id)

        if job is None:

            return {
                "success": False,
                "message": "Job Not Found"
            }

        return {
            "success": True,
            "job": job
        }