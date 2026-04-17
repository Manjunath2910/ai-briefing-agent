import feedparser

# ✅ AI-focused sources (reliable)
SOURCES = [
    "https://hnrss.org/newest?q=AI",
    "https://hnrss.org/newest?q=llm",
    "https://hnrss.org/newest?q=agents",   # ✅ better than 'agent'
    "https://hnrss.org/newest?q=machine%20learning"
]

def fetch_rss():
    items = []

    for url in SOURCES:
        print(f"Fetching: {url}")

        feed = feedparser.parse(
            url,
            request_headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        if not feed.entries:
            print(f"❌ No entries from: {url}")
            continue

        print(f"✅ Found {len(feed.entries)} items")

        for entry in feed.entries:
            title = entry.get("title", "")
            link = entry.get("link", "")
            summary = entry.get("summary", "")

            # ✅ Basic validation
            if not title or not link:
                continue

            items.append({
                "title": title,
                "link": link,
                "summary": summary
            })

    return items
