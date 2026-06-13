from tools.search import search_web

def run_agent(query: str):
    print("\n[DEBUG] Query:", query)

    results = search_web(query)

    formatted = []

    for r in results:
        title = r.get("title", "")
        url = r.get("url", "")
        content = r.get("content", "")

        # clean + skip bad entries
        if not title or not url:
            continue

        formatted.append({
            "title": title.strip(),
            "url": url.strip(),
            "summary": content.strip()[:250]
        })

    # limit results for clean UI
    return formatted[:5]


if __name__ == "__main__":
    test = run_agent("AI agents")
    print("\nFINAL OUTPUT:\n", test)