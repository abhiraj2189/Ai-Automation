from collector import get_ai_news
from saver import save_ai_tools

news = get_ai_news()

print("=" * 70)
print("LATEST AI UPDATES")
print("=" * 70)

for i, item in enumerate(news, start=1):

    print(f"\n{i}. {item['title']}")
    print("Source :", item["source"])
    print(item["link"])

save_ai_tools(news)