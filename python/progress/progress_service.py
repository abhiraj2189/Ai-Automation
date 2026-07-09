from python.progress.progress_manager import ProgressManager


class ProgressService:

    def status(

        self,

        job_id

    ):

        return ProgressManager.get(job_id)