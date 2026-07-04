import json
import os


def save_ai_tools(data):

    folder = "../../../data/ai_tools"

    os.makedirs(folder, exist_ok=True)

    file_path = os.path.join(folder, "ai_tools.json")

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("\n✅ AI Tools Saved Successfully")
    print(file_path)