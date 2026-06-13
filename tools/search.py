from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query: str):
    response = client.search(query=query, search_depth="basic")

    results = []

    for r in response.get("results", []):
        results.append({
            "title": r.get("title"),
            "url": r.get("url"),
            "content": r.get("content")
        })

    return results


if __name__ == "__main__":
    results = search_web("AI agents latest trends")

    for r in results[:3]:
        print("\nTITLE:", r["title"])
        print("URL:", r["url"])
        print("CONTENT:", r["content"][:200])
