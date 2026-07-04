from collector import get_news
from saver import save_news

news = get_news()

print("=" * 60)
print("LATEST TECH NEWS")
print("=" * 60)

for i, item in enumerate(news, start=1):
    print(f"\n{i}. {item['title']}")
    print(item['link'])

save_news(news)