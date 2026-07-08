from python.projects.project_repository import ProjectRepository


class ProjectService:

    def save(self, project):

        repo = ProjectRepository()

        repo.save(project)

        return {
            "success": True
        }