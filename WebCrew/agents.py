import os
from crewai import Agent
from dotenv import load_dotenv
from tools import tool
load_dotenv()

#now i am going to create agent1
google_api_key=os.getenv('GOOGLE_API_KEY')
from langchain_google_genai import  ChatGoogleGenerativeAI
llm=ChatGoogleGenerativeAI(model="gemini-pro",
                           verbose=True,
                           temprature=0.5,
                           google_api_key=google_api_key,)

github_summarizer=Agent(
    role='github content provider',
    goal='As a professional github reader you task is to provide content and code from github {topic}',
    backstory='',
    tool=[tool],
    llm=llm,
    verbose=True,
    allow_delegation=False,
)