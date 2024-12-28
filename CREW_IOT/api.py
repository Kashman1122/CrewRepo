import os
import re
from dotenv import load_dotenv
from crewai import Crew, Agent, Task, Process
from crewai_tools import SerperDevTool
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

# Load API keys from environment
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')

# Configure the Google Generative AI model
genai.configure(api_key=google_api_key)
llm = GoogleGenerativeAI(api_key=os.getenv("GOOGLE_API_KEY"), model='gemini-1.5-pro')

# Define the tool using SerperDevTool
tool = SerperDevTool()

# Define the agent responsible for finding innovative ideas
latest_innovator_agent = Agent(
    role="Innovative Idea Finder",
    goal="Your goal is to find the top 5 innovative ideas including research paper and patent links based on provided {input}.",
    backstory=("A creative virtual assistant with a deep understanding of emerging trends and technologies, "
               "skilled at discovering innovative ideas based on user prompts."),
    llm=llm,
    tools=[tool],
    allow_delegation=False,
)

# Define the task for dataset provider
dataset_provider = Task(
    description="Your Task is to provide top 5 research papers and patent links based on the provided {input}.",
    expected_output="The expected output should be the patents and research paper links related to the given idea.",
    tools=[tool],
    agent=latest_innovator_agent,
)

# Configure CrewAI with the agent and task
crew = Crew(
    agents=[latest_innovator_agent],
    tasks=[dataset_provider],
    process=Process.sequential,
)

# Function to fetch innovative ideas
def get_innovative_ideas(user_input):
    try:
        # Run the Crew process with the provided input
        result = crew.kickoff(inputs={'input': user_input})

        # If results are obtained, extract and return links
        raw_text = result[0]['output'] if result and 'output' in result[0] else ""
        links = re.findall(r'(https?://\S+)', raw_text)
        top_links = links[:5]  # Limit to top 5 links

        return {"top_5_links": top_links}
    except Exception as e:
        return {"error": str(e)}

# Test the function with a sample input
if __name__ == "__main__":
    user_input = "working on portable device that can connect with any device and tell the energy consumption with bill"
    output = get_innovative_ideas(user_input)
    print(output)
