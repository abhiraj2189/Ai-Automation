import json
import os


def save_news(news):

    folder = "../../../data/news"

    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, "latest_news.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(news, file, indent=4, ensure_ascii=False)

    print(f"\n✅ News Saved Successfully")
    print(file_path)