def generate_briefing(items):
    message = "Good morning ☀️\n\n"

    # 🔥 Top signal (first item)
    top = items[0]
    message += f"🔥 Top signal:\n{top['title']}\n"
    message += f"{top['url']}\n"
    message += "Why it matters: This directly impacts how you design and build AI agents.\n\n"

    # ⚡ Supporting signals
    message += "⚡ Also worth your attention:\n\n"

    for item in items[1:]:
        message += f"- {item['title']}\n"
        message += f"  {item['url']}\n\n"

    # 🧠 Insight
    message += "🧠 Insight:\n"
    message += "There is a strong trend toward multi-agent systems and autonomous workflows. Focus on architecture and memory.\n\n"

    # 🎯 Action
    message += "👉 Today's Action:\n"
    message += "Read the top signal and apply ONE concept in your project today.\n"

    return message
