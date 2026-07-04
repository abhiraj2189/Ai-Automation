import requests
import json

url = "https://api.github.com"

response = requests.get(url)

data = response.json()

with open("../data/github_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("GitHub data saved successfully!")