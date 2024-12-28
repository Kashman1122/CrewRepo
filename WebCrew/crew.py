from agents import web_summarizer
from tasks import summarize_task
from crewai.process import Process
from crewai import Crew



# Define the crew
crew = Crew(
    agents=[web_summarizer],
    tasks=[summarize_task],
    process=Process.sequential,
)


# Kick off the crew process with the YouTube video URL as input
# Kick off the crew process with the website URL as input
result = crew.kickoff(inputs={'type': 'provide all code'})
print(result)

