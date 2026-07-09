import threading

from python.jobs.job_manager import JobManager
from python.studio.workflow_service import WorkflowService


class Worker:

    @staticmethod
    def start(

        job_id: str,

        topic: str

    ):

        thread = threading.Thread(

            target=Worker.run,

            args=(job_id, topic),

            daemon=True

        )

        thread.start()

    @staticmethod
    def run(

        job_id: str,

        topic: str

    ):

        try:

            JobManager.update(

                job_id,

                5,

                "Starting"

            )

            workflow = WorkflowService()

            result = workflow.run(

                topic=topic,

                job_id=job_id

            )

            output = result.get(

                "video",

                None

            )

            JobManager.complete(

                job_id,

                output

            )

        except Exception as e:

            JobManager.failed(

                job_id,

                str(e)

            )