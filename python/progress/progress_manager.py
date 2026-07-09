class ProgressManager:

    progress = {}

    @classmethod
    def create(cls, job_id):

        cls.progress[job_id] = {

            "status": "Pending",

            "progress": 0,

            "step": "Waiting"

        }

    @classmethod
    def update(

        cls,

        job_id,

        step,

        progress,

        status="Running"

    ):

        cls.progress[job_id] = {

            "status": status,

            "progress": progress,

            "step": step

        }

    @classmethod
    def complete(

        cls,

        job_id

    ):

        cls.progress[job_id] = {

            "status": "Completed",

            "progress": 100,

            "step": "Done"

        }

    @classmethod
    def get(

        cls,

        job_id

    ):

        return cls.progress.get(job_id)