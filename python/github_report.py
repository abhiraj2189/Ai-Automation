import requests

username = "abhiraj2189"

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

data = response.json()

print("=" * 60)
print("           GITHUB PROFILE REPORT")
print("=" * 60)

print(f"👤 Name           : {data['name']}")
print(f"💻 Username       : {data['login']}")
print(f"📦 Public Repos   : {data['public_repos']}")
print(f"👥 Followers      : {data['followers']}")
print(f"➡️ Following      : {data['following']}")
print(f"📅 Account Created: {data['created_at']}")
print(f"🌐 Profile URL    : {data['html_url']}")
print(f"📝 Bio            : {data['bio']}")

print("=" * 60)