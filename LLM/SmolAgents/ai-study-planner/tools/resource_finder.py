from smolagents.tools import tool
import os
import requests

@tool
def resource_finder(subtopic: str) -> list:
    """
    Finds resources for each subtopic using the Tavily Search API.

    Args:
        subtopic (str): The subtopic to find resources for

    Returns:
        list: A list of top resource titles and links
    """
    TAVILY_API_KEY = "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"

    url = "https://api.tavily.com/search"
    headers = {"Content-Type": "application/json"}
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": subtopic,
        "search_depth": "basic",
        "max_results": 3
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()

    return [f"{item['title']} - {item['url']}" for item in data.get("results", [])[:3]]

    
