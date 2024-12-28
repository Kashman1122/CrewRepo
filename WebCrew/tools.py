import os
from crewai_tools import GithubSearchTool
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
google_api_key = os.getenv('GOOGLE_API_KEY')
github_token = os.getenv('GITHUB_TOKEN')  # Ensure this environment variable is set

# Initialize the LLM with the correct configuration
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    verbose=True,
    temperature=0.5,
    google_api_key=google_api_key,
)

# Initialize the tool for semantic searches within a specific GitHub repository
tool = GithubSearchTool(
    type='code',
    llm=llm,
    github_repo='https://github.com/ultralytics/yolov5/tree/master/classify',
    content_types=['code', 'issue']  # Options: code, repo, pr, issue
)

# Set the GitHub token for authentication
tool.set_github_token(github_token)

# Now you can use the `tool` for GitHub search operations
