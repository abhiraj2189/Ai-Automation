import json

with open("../data/github_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("===== GitHub Information =====\n")

print("Current User URL :", data["current_user_url"])
print("Repository URL   :", data["repository_url"])
print("Issues URL       :", data["repository_url"])
print("Rate Limit URL   :", data["rate_limit_url"])
