from smolagents.tools import tool

@tool
def schedule_week(subtopics: list) -> dict:
    """
    Break down a topic into learning concept for 14 days.
    
    Args:
        subtopics (list): The subtopics to be scheduled for each day.

    Returns:
        dict: A dict of 14 day schedule.
    """
    return {f"Day {i+1}": topic for i, topic in enumerate(subtopics)}
