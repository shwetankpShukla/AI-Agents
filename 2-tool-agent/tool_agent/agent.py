from datetime import datetime
from google.adk.agents import Agent 
from google.adk.tools import google_search
from dotenv import load_dotenv
import os


# Specify full path to your .env file
env_path = '/Users/shwetank/Agent/2-tool-agent/tool_agent/.env'
load_dotenv(dotenv_path=env_path)  # Loads variables from specified .env file into os.environ
# Now you can access the environment variables

print("Loaded GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))

def get_current_time() -> dict:
    """Returns the current time in format YYYY-MM-DD HH:MM:SS"""
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search
    """,
    tools=[google_search],
    #functions=[get_current_time],

    # tools=[get_current_time],
    # tools=[google_search, get_current_time], # <--- Doesn't work
    #max_iterations=3,
    #max_iterations_per_tool=1,
    #max_iterations_per_function=1,
)