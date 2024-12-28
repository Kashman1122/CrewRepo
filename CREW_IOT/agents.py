from crewai import Agent
from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv
from tools import tool
load_dotenv()

# Initialize Google Generative AI
llm = GoogleGenerativeAI(api_key=os.getenv("GOOGLE_API_KEY"), model='gemini-1.5-pro')

# Create IOT Research Agent
iot_research_agent = Agent(
    role="Innovative Idea Finder",
    goal="Your goal is to find the top 5 innovative research paper and patent links based on provided {input}.",
    backstory=("A creative virtual assistant with a deep understanding of emerging trends and technologies, "
               "skilled at discovering innovative ideas based on user prompts."),
    llm=llm,
    tools=[tool],
    allow_delegation=False,
)
