from smolagents.tools import tool
import requests

def run_ollama(prompt: str, model: str = "llama3") -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    response.raise_for_status()
    return response.json()["response"]

@tool
def topic_breakdown(topic: str) -> list:
    """
    Uses LLaMA 3 via Ollama to break the topic into 14 subtopics.
     Args:
        topic (str): The topic to find resource for

    Returns:
        list: A list of subtopics for the topic.
    """
    prompt = f"Break down the topic '{topic}' into 14 subtopics for a structured 14-day study plan."
    response = run_ollama(prompt)

    # Parse into a clean list
    return [line.strip("-•1234567890. ").strip() for line in response.split("\n") if line.strip()]
