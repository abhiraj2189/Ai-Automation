import json
import os

file_path = "../../../data/news/latest_news.json"

if not os.path.exists(file_path):
    print("❌ News file not found.")
    exit()

with open(file_path, "r", encoding="utf-8") as file:
    news = json.load(file)

print("=" * 60)
print("NEWS ANALYSIS")
print("=" * 60)

print(f"📰 Total News : {len(news)}")

titles = set()

duplicate = 0

for item in news:

    if item["title"] in titles:
        duplicate += 1

    titles.add(item["title"])

print(f"✅ Unique News : {len(titles)}")
print(f"⚠ Duplicate News : {duplicate}")

print("\nTop Headlines\n")

for i, item in enumerate(news[:5], start=1):
    print(f"{i}. {item['title']}")