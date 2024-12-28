from crewai import Task
from tools import tool  # Import your tool
from agents import iot_research_agent  # Import your agent

# Define your task
iot_research_task = Task(
    description="Your Task is to provide top 5 research papers and patent links from google similar to the provided {input}.",
    expected_output="The expected output should be the patents and research paper links related to the given idea.",
    tools=[tool],
    agent=iot_research_agent,
)

# Example usage:
# You can now use iot_research_task to define and manage specific tasks related to IOT research and error troubleshooting.
