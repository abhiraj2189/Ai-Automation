from coding_collector import get_coding_news
from coding_saver import save_coding_news

news = get_coding_news()

print("=" * 60)
print("LATEST CODING NEWS")
print("=" * 60)

for i, item in enumerate(news, start=1):
    print(f"\n{i}. {item['title']}")
    print(item["link"])

save_coding_news(news)