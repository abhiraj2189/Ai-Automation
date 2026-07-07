from python.studio.workflow_service import WorkflowService


class StudioService:

    def generate(self, topic: str):

        workflow = WorkflowService()

        return workflow.run(topic)