import json

with open("../../../data/ai_tools/ai_tools.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for item in data[:5]:
    print(item["title"])