import feedparser
import pymongo
from datetime import datetime

# Daftar sumber RSS
rss_sources = [
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://www.theguardian.com/world/rss"
]

def fetch_rss(rss_url):
    try:
        print(f"Fetching from: {rss_url}")
        feed = feedparser.parse(rss_url)

        if not feed.entries:
            print(f"⚠️  No entries found for: {rss_url}")
            return []

        articles = []
        for entry in feed.entries:
            article = {
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "summary": entry.get("summary", ""),
                "published": entry.get("published", ""),
                "source": rss_url,
                "scraped_at": datetime.utcnow()
            }
            articles.append(article)

        print(f"✅ Found {len(articles)} articles from: {rss_url}")
        return articles

    except Exception as e:
        print(f"❌ Failed to fetch from {rss_url}: {e}")
        return []

def save_to_mongodb(articles):
    if not articles:
        print("⚠️  No articles to save.")
        return

    client = pymongo.MongoClient("mongodb://mongo:27017")  # untuk Docker
    db = client["fakenews"]
    collection = db["clean_news_raw"]
    collection.insert_many(articles)
    print(f"💾 Saved {len(articles)} articles to MongoDB.")

if __name__ == "__main__":
    total = 0
    for rss in rss_sources:
        news = fetch_rss(rss)
        save_to_mongodb(news)
        total += len(news)

    if total == 0:
        print("📭 No articles found from all sources.")
    else:
        print(f"🎉 Done. Total articles collected: {total}")
