import requests

url = "https://api.github.com"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("\nGitHub API Response:\n")

print(data)

print(type(data))
print("\n===== Selected Data =====")

print("Current User URL :", data["current_user_url"])
print("Repository URL   :", data["repository_url"])
print("Rate Limit URL   :", data["rate_limit_url"])