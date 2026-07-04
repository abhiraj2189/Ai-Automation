from python.database.database_manager import DatabaseManager


class GitHubSaver:

    def __init__(self):
        self.db = DatabaseManager()

    def save_user(self, user):
        self.db.save("github", "user.json", user)

    def save_repositories(self, repositories):
        self.db.save("github", "repositories.json", repositories)