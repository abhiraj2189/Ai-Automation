import feedparser


def read_rss(url):
    return feedparser.parse(url)