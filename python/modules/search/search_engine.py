import json


class SearchEngine:

    def search(self, file_path, keyword):

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        result = []

        keyword = keyword.lower()

        for item in data:

            text = json.dumps(item).lower()

            if keyword in text:
                result.append(item)

        return result