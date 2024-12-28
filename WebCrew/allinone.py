import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import WebsiteSearchTool
from crewai import Agent, Task, Crew
from crewai.process import Process

# Load environment variables
load_dotenv()

# Retrieve Google API key from environment variables
google_api_key = os.getenv('GOOGLE_API_KEY')

# Initialize the LLM with the correct configuration
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=google_api_key,
)

# Initialize the website search tool
tool = WebsiteSearchTool(
    llm=llm,
    embedder=dict(
        provider="google",
        config=dict(
            model="models/embedding-001",
            task_type="retrieval_document",
        ),
    ),
)

# Create the web summarizer agent
web_summarizer = Agent(
    role='Website Summarizer',
    goal='As a professional web reader your task is to summarize the website {topic}',
    backstory='',
    tool=[tool],
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# Define the summarization task
summarize_task = Task(
    description=(
        "Identify the website {topic}",
        "Get detailed information about the website from the website link."
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of the website content.',
    tools=[tool],
    agent=web_summarizer,
)

# Define the crew
crew = Crew(
    agents=[web_summarizer],
    tasks=[summarize_task],
    process=Process.sequential,
)

# Kick off the crew process with the website URL as input
result = crew.kickoff(inputs={'website_url': 'https://docs.crewai.com/tools/WebsiteSearchTool/#description'})
print(result)
