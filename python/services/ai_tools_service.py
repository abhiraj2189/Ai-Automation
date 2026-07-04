from python.repositories.ai_tools_repository import AIToolsRepository


class AIToolsService:

    def get_tools(self):

        repo = AIToolsRepository()

        return repo.get_all()