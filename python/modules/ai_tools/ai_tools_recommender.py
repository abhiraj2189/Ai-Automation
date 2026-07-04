import json
import os

FILE_PATH = "../../../data/ai_tools/ai_tools_database.json"


def load_database():
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def recommend(category):

    data = load_database()

    category = category.lower()

    print("\n" + "=" * 70)
    print(f"BEST AI TOOLS FOR {category.upper()}")
    print("=" * 70)

    found = False

    for tool in data:

        if tool["category"].lower() == category:

            print(f"\n🤖 {tool['name']}")
            print(f"🏢 Company : {tool['company']}")
            print(f"💰 Price   : {tool['price']}")
            print(f"🎯 Best For: {', '.join(tool['best_for'])}")
            print(f"🌐 Website : {tool['website']}")

            found = True

    if not found:
        print("\nNo recommendation found.")


print("Select Category")
print("1. Student")
print("2. Developer")
print("3. Professional")

choice = input("\nEnter Choice : ")

if choice == "1":
    recommend("Student")

elif choice == "2":
    recommend("Developer")

elif choice == "3":
    recommend("Professional")

else:
    print("Invalid Choice")