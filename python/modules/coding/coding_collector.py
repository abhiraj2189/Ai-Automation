import feedparser

RSS_URL = "https://www.freecodecamp.org/news/rss/"


def get_coding_news():
    feed = feedparser.parse(RSS_URL)

    news = []

    for article in feed.entries[:10]:
        news.append({
            "title": article.title,
            "link": article.link
        })

    return news