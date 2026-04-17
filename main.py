from fetch_rss import fetch_rss
from clean import clean_items
from score import score_items
from briefing import generate_briefing

def run():
    print("Fetching RSS...")
    raw = fetch_rss()

    # Debug (optional)
    print(f"\nTotal raw items: {len(raw)}")

    print("Cleaning data...")
    clean = clean_items(raw)
    print(f"Total clean items: {len(clean)}")

    if not clean:
        print("❌ No data after cleaning. Check RSS or filters.")
        return

    print("Scoring items...")
    scores = score_items(clean)

    print("\nScores:\n", scores)

    # ✅ FILTER: Only high-quality items
    filtered_scores = [item for item in scores if item["score"] >= 4]

    # ✅ FALLBACK (if too strict)
    if len(filtered_scores) < 3:
        print("⚠️ Not enough high-score items, using fallback...")
        filtered_scores = scores[:3]

    # ✅ Pick top 3
    top_items = [clean[item["id"]] for item in filtered_scores[:3]]

    print("\nTop Selected Items:\n")
    for item in top_items:
        print("-", item["title"])

    # ✅ Generate final briefing
    briefing = generate_briefing(top_items)

    print("\n=== FINAL BRIEFING ===\n")
    print(briefing)


if __name__ == "__main__":
    run()
