import json
import os


class ReportGenerator:

    def count_records(self, file_path):

        if not os.path.exists(file_path):
            return 0

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, list):
            return len(data)

        return 1

    def generate(self):

        print("=" * 60)
        print("AI AUTOMATION REPORT")
        print("=" * 60)

        files = {

            "AI Tools":
            "data/ai_tools/ai_tools.json",

            "GitHub Users":
            "data/github/user.json",

            "Repositories":
            "data/github/repositories.json",

            "Coding News":
            "data/coding/coding_news.json",

            "AI News":
            "data/news/ai_news.json"

        }

        for title, path in files.items():

            total = self.count_records(path)

            print(f"{title:<20}: {total}")

        print("\nReport Generated Successfully")