import feedparser

RSS_FEEDS = [
    "https://www.marktechpost.com/feed/",
    "https://openai.com/news/rss.xml",
    "https://huggingface.co/blog/feed.xml"
]


def get_ai_news():

    all_news = []

    for rss in RSS_FEEDS:

        feed = feedparser.parse(rss)

        for article in feed.entries[:10]:

            all_news.append({
                "title": article.title,
                "link": article.link,
                "source": feed.feed.get("title", "Unknown")
            })

    return all_news