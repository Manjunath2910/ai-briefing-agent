NOISE_KEYWORDS = [
    "hiring",
    "job",
    "career",
    "yc",
    "launch hn",
    "show hn",
    "we are hiring"
]

def clean_items(items):
    seen = set()
    clean = []

    for item in items:
        if item["link"] in seen:
            continue

        seen.add(item["link"])

        title_lower = item["title"].lower()

        # 🚫 Filter noise
        if any(keyword in title_lower for keyword in NOISE_KEYWORDS):
            continue

        clean.append({
            "title": item["title"],
            "url": item["link"],
            "text": item["summary"][:300]
        })

    return clean
