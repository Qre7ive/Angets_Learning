import os

from dotenv import load_dotenv
from serpapi import SerpApiClient

load_dotenv()


def search(query: str) -> str:
    """
    A SerpApi-backed web search tool that returns concise search results.
    """
    print(f"[SerpApi] Searching: {query}")
    try:
        api_key = os.getenv("SERPAPI_API_KEY")
        if not api_key:
            return "Error: SERPAPI_API_KEY is not configured in .env."

        params = {
            "engine": "google",
            "q": query,
            "api_key": api_key,
            "gl": "cn",
            "hl": "zh-cn",
        }

        client = SerpApiClient(params)
        results = client.get_dict()

        if "answer_box_list" in results:
            answer_box_list = results["answer_box_list"]
            if isinstance(answer_box_list, list):
                return "\n".join(str(item) for item in answer_box_list)

        if "answer_box" in results and "answer" in results["answer_box"]:
            return str(results["answer_box"]["answer"])

        if "knowledge_graph" in results and "description" in results["knowledge_graph"]:
            return str(results["knowledge_graph"]["description"])

        if "organic_results" in results and results["organic_results"]:
            snippets = [
                f"[{i + 1}] {res.get('title', '')}\n{res.get('snippet', '')}"
                for i, res in enumerate(results["organic_results"][:3])
            ]
            return "\n\n".join(snippets)

        return f"No information found for: {query}"
    except Exception as e:
        return f"Search failed: {e}"
