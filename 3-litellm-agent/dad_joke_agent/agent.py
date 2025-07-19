import os
import random

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv

# Specify full path to your .env file
#env_path = '/Users/shwetank/Agent/3-litellm-agent/dad_joke_agent/.env'
#load_dotenv(dotenv_path=env_path)  # Loads variables from specified .env file into os.environ
# Now you can access the environment variables
load_dotenv() 
print("Loaded OPENROUTER_API_KEY:", os.getenv("OPENROUTER_API_KEY"))

model = LiteLlm(
    #https://docs.litellm.ai/docs/providers/openrouter
    model="openrouter/openai/gpt-4.1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

def get_dad_joke():
    jokes =[
        "🤣 2. Papa: Heeralal, homework kiya? Heeralal: Nahi papa, teacher ne bola kal se karna. Papa: Teacher ne kab bola? Heeralal: Jab main soch raha tha wo tab bola hoga. 😆",
        "🤣 3. Heeralal: Papa, aap mujhse kitna pyaar karte ho? Papa: Chaand tak aur wapas. Heeralal: Par papa, aap to petrol bharwate nahi itna… Papa: Beta, ye toh sirf example tha. 😅",
        "🤣 4. Papa: Heeralal, jaldi uth ja, school ka time ho gaya. Heeralal: Papa, aapko kaise pata subah ho gayi? Papa: Kyuki meri chai thandi ho gayi. 😂",
        "🤣 5. Heeralal: Papa mujhe ek magic dikhana hai. Papa: Kaunsa magic beta? Heeralal: Dekho homework disappear… Papa: Aur ab dekho teri chhutti bhi disappear. 🤣",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
    ]
    return random.choice(jokes)

root_agent = Agent(
        name="dad_joke_agent",
        model=model,
        description="Dad joke agent",
        instruction="""
        You are a helpful assistant that can tell dad jokes. 
        Only use the tool `get_dad_joke` to tell jokes.
        """,
        tools=[get_dad_joke],
)