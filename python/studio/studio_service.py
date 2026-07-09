from python.studio.workflow_service import WorkflowService


class StudioService:

    def generate(
        self,
        topic: str,
        job_id: str | None = None
    ):

        workflow = WorkflowService()

        return workflow.run(

            topic=topic,

            job_id=job_id

        )