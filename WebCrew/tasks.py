from agents import github_summarizer
from tools import tool
from crewai import Task

summarize_task=Task(
description=(
        "identify the website {topic}",
        "Get the detailed information about the website from the website link."
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of the github repositry.',
    tools=[tool],
    agent=github_summarizer,
)