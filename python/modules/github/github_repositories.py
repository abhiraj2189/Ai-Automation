import requests


class GitHubRepositories:

    BASE_URL = "https://api.github.com/users"

    def get_repositories(self, username):

        url = f"{self.BASE_URL}/{username}/repos"

        response = requests.get(url, timeout=30)

        if response.status_code == 200:
            return response.json()

        return []