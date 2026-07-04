import requests

username = "abhiraj2189"

url = "https://api.github.com/users/abhiraj2189"

response = requests.get(url)

data = response.json()

print("=" * 50)
print("GitHub User Information")
print("=" * 50)

print("Name        :", data["name"])
print("Username    :", data["login"])
print("Followers   :", data["followers"])
print("Following   :", data["following"])
print("Public Repo :", data["public_repos"])
print("Profile URL :", data["html_url"])
print("Bio         :", data["bio"])