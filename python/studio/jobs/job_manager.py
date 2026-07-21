from python.studio.jobs.job_store import JobStore


class JobManager:

    @staticmethod
    def create():

        return JobStore.create()


    @staticmethod
    def update(job_id, progress, status):

        job = JobStore.get(job_id)

        if job:

            job["progress"] = progress
            job["status"] = status


    @staticmethod
    def complete(job_id, video):

        job = JobStore.get(job_id)

        if job:

            job["progress"] = 100
            job["status"] = "Completed"
            job["video"] = video


    @staticmethod
    def failed(job_id, error):

        job = JobStore.get(job_id)

        if job:

            job["status"] = "Failed"
            job["error"] = error
    @staticmethod
    def get(job_id):

         return JobStore.get(job_id)