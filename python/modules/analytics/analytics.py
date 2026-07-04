import json
from pathlib import Path


class Analytics:

    def __init__(self):
        self.root = Path(__file__).resolve().parents[3]
        self.data = self.root / "data"

    def count(self, folder, file_name):
        file_path = self.data / folder / file_name

        if not file_path.exists():
            return 0

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return len(data)

        return 1

    def run(self):

        report = {
            "github_users": self.count("github", "github_users.json"),
            "ai_tools": self.count("ai_tools", "ai_tools.json"),
            "coding_news": self.count("coding", "coding_news.json"),
            "ai_news": self.count("news", "ai_news.json")
        }

        save_path = self.data / "analytics" / "analytics.json"

        with open(save_path, "w", encoding="utf-8") as file:
            json.dump(report, file, indent=4)

        print("\n===== ANALYTICS =====")

        for key, value in report.items():
            print(f"{key} : {value}")