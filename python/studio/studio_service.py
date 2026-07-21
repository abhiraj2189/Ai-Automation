from python.studio.workflow_service import WorkflowService
from python.studio.jobs.job_manager import JobManager


class StudioService:

    def generate(self, topic: str):

        job_id = JobManager.create()

        workflow = WorkflowService()

        workflow.run(

            topic=topic,

            job_id=job_id

        )

        return {

            "job_id":job_id,

            "message":"Workflow Started"

        }