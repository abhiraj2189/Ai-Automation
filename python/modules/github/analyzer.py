import json
import os

file_path = "../../../data/github_users.json"

if os.path.exists(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    print("=" * 60)
    print("        GITHUB USER ANALYSIS")
    print("=" * 60)

    # Agar list hai to pehla user lo
    if isinstance(data, list):
        user = data[0]
    else:
        user = data

    print("Name         :", user.get("name"))
    print("Username     :", user.get("login"))
    print("Followers    :", user.get("followers"))
    print("Following    :", user.get("following"))
    print("Public Repos :", user.get("public_repos"))
    print("Profile URL  :", user.get("html_url"))

else:
    print("❌ github_users.json file not found.")