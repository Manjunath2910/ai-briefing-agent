KEYWORDS_STRONG = [
    "agent", "agentic", "autonomous", "multi-agent"
]

KEYWORDS_MEDIUM = [
    "ai", "llm", "gpt", "model", "machine learning",
    "deep learning", "neural"
]

KEYWORDS_BUILD = [
    "build", "framework", "tool", "api", "sdk",
    "automation", "workflow", "python"
]

def score_items(items):
    scored = []

    for i, item in enumerate(items):
        text = (item["title"] + " " + item["text"]).lower()

        score = 0

        # 🔥 Strong signals (core goal)
        for kw in KEYWORDS_STRONG:
            if kw in text:
                score += 5

        # ⚡ Medium signals
        for kw in KEYWORDS_MEDIUM:
            if kw in text:
                score += 3

        # 🛠 Build-related
        for kw in KEYWORDS_BUILD:
            if kw in text:
                score += 2

        scored.append({
            "id": i,
            "score": score,
            "title": item["title"]
        })

    return sorted(scored, key=lambda x: x["score"], reverse=True)
