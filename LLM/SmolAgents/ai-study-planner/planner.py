from smolagents import CodeAgent
from smolagents.models import Model
from tools.schedule_week import schedule_week
from tools.resource_finder import resource_finder
from tools.topic_breakdown import topic_breakdown
import requests
import os


def create_study_planner():
    return CodeAgent(
        name="study_planner",
        description="Generate a 14-day study plan using a local Ollama model.",
        tools=[topic_breakdown, schedule_week, resource_finder],
        model=None
    )

if __name__ == "__main__":
    topic = input("Enter a topic for your study plan: ")
    subtopics = topic_breakdown(topic)

    schedule = schedule_week(subtopics)

    print("\n📚 Your Study Plan:\n")
    for day, subtopic in schedule.items():
        print(f"{subtopic}")
        links = resource_finder(subtopic)
        for link in links:
            print(f"   🔗 {link}")

