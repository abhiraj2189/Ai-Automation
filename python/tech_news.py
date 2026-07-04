import feedparser

rss_url = "https://feeds.feedburner.com/TheHackersNews"

feed = feedparser.parse(rss_url)

print("=" * 60)
print("LATEST TECH NEWS")
print("=" * 60)

for i, entry in enumerate(feed.entries[:10], start=1):
    print(f"\n{i}. {entry.title}")
    print(f"Link : {entry.link}")