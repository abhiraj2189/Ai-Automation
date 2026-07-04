import requests

username = input("Enter GitHub Username: ")

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\n" + "=" * 60)
    print("         GITHUB PROFILE ANALYZER")
    print("=" * 60)

    print(f"👤 Name            : {data['name']}")
    print(f"💻 Username        : {data['login']}")
    print(f"📦 Public Repos    : {data['public_repos']}")
    print(f"👥 Followers       : {data['followers']}")
    print(f"➡️ Following       : {data['following']}")
    print(f"📅 Created At      : {data['created_at']}")
    print(f"🌐 Profile URL     : {data['html_url']}")
    print(f"📝 Bio             : {data['bio']}")

    print("=" * 60)

else:
    print("❌ GitHub user not found.")