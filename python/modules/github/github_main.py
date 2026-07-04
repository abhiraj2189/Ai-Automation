from python.modules.github.github_collector import GitHubCollector
from python.modules.github.github_repositories import GitHubRepositories
from python.modules.github.github_saver import GitHubSaver

collector = GitHubCollector()
repositories = GitHubRepositories()
saver = GitHubSaver()

username = input("GitHub Username : ")

user = collector.get_user(username)

if user is None:
    print("❌ User Not Found")
    exit()

repo_list = repositories.get_repositories(username)

saver.save_user(user)
saver.save_repositories(repo_list)

print("\n✅ User Saved")
print("✅ Repositories Saved")

print("\n========== USER ==========")
print("Name :", user.get("name"))
print("Followers :", user.get("followers"))
print("Public Repositories :", user.get("public_repos"))

print("\n========== TOP REPOSITORIES ==========")

for repo in repo_list[:10]:
    print(f"\n📦 {repo['name']}")
    print(f"⭐ Stars : {repo['stargazers_count']}")
    print(f"💻 Language : {repo['language']}")