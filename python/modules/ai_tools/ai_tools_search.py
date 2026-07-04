import json
import os

FILE_PATH = "../../../data/ai_tools/ai_tools_database.json"


def load_data():
    if not os.path.exists(FILE_PATH):
        print("Database not found!")
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def search_tools(keyword):

    keyword = keyword.lower()

    data = load_data()

    found = False

    for tool in data:

        if (
            keyword in tool["name"].lower()
            or keyword in tool["company"].lower()
            or keyword in tool["category"].lower()
            or keyword in tool["price"].lower()
            or any(keyword in item.lower() for item in tool["best_for"])
        ):

            print("=" * 70)
            print("Name      :", tool["name"])
            print("Company   :", tool["company"])
            print("Category  :", tool["category"])
            print("Price     :", tool["price"])
            print("Best For  :", ", ".join(tool["best_for"]))
            print("Website   :", tool["website"])
            print("=" * 70)

            found = True

    if not found:
        print("\nNo matching AI tool found.")


if __name__ == "__main__":

    keyword = input("Search : ")

    search_tools(keyword)