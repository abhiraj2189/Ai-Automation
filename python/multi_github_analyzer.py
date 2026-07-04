import requests
import json

# List of GitHub usernames
usernames = [
    "octocat",
    "abhiraj2189",
    "torvalds",
    "microsoft"
]

all_users = []

for username in usernames:

    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        user_info = {
            "name": data["name"],
            "username": data["login"],
            "followers": data["followers"],
            "following": data["following"],
            "public_repos": data["public_repos"],
            "profile": data["html_url"]
        }

        all_users.append(user_info)

with open("../data/github_users.json", "w", encoding="utf-8") as file:
    json.dump(all_users, file, indent=4)

print("✅ All GitHub users saved successfully!")