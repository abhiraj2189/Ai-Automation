import json
from helper import print_title

with open("../../../data/github_users.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print_title("GITHUB REPORT")

if isinstance(data, list):
    for user in data:
        print(f"👤 {user.get('name')}")
        print(f"💻 {user.get('username')}")
        print(f"👥 Followers : {user.get('followers')}")
        print(f"📦 Repositories : {user.get('public_repos')}")
        print("-" * 60)
else:
    print("No Data Found")