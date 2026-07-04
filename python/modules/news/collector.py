import feedparser


def get_news():

    rss_url = "https://feeds.feedburner.com/TheHackersNews"

    feed = feedparser.parse(rss_url)

    news = []

    for article in feed.entries[:10]:

        news.append(
            {
                "title": article.title,
                "link": article.link
            }
        )

    return news