import json
import os

def save_coding_news(news):

    base_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../../")
    )

    data_folder = os.path.join(base_dir, "data", "coding")
    os.makedirs(data_folder, exist_ok=True)

    file_path = os.path.join(data_folder, "coding_news.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(news, file, indent=4, ensure_ascii=False)

    print(f"\n✅ Coding News Saved")
    print(f"📂 Saved at: {file_path}")