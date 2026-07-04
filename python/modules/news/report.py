import json

with open("../../../data/news/latest_news.json", "r", encoding="utf-8") as file:
    news = json.load(file)

print("=" * 60)
print("DAILY NEWS REPORT")
print("=" * 60)

for i, item in enumerate(news, start=1):
    print(f"\n{i}. {item['title']}")
    print(item['link'])