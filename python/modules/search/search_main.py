from python.modules.search.search_engine import SearchEngine

engine = SearchEngine()

keyword = input("Search : ")

result = engine.search(
    "data/ai_tools/ai_tools.json",
    keyword
)

print()

print("=" * 60)

print("FOUND", len(result), "RESULTS")

print("=" * 60)

for item in result:

    print()

    print(item["name"])

    print(item["category"])

    print(item["website"])