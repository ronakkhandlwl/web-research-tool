import requests
import os


def web_search(query, max_results=3):
    """
    Perform a Google search using SerpAPI and return formatted results.

    Args:
        query: Search query string
        max_results: Maximum number of results to return
        api_key: Your SerpAPI key (required)

    Returns:
        List of dicts with each result containing title, link, and snippet
    """
    api_key = os.getenv('SERP_API_KEY')
    if not api_key:
        raise ValueError("API key is required for SerpAPI")

    # Set up the API request
    base_url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key,
        "num": max_results
    }

    formatted_results = []

    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract and format organic results
        if "organic_results" in data:
            for result in data["organic_results"][:max_results]:
                formatted_results.append({
                    "title": result.get("title", ""),
                    "link": result.get("link", ""),
                    "snippet": result.get("snippet", "")
                })

        return formatted_results

    except requests.exceptions.RequestException as e:
        print(f"Error making request to SerpAPI: {e}")
        return []
