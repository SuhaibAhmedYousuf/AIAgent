from agno.agent import Agent
from agno.models.groq import Groq 
from agno.tools.duckduckgo import DuckDuckGoTools
# from agno.models.openai import OpenAIChat

import os
from dotenv import load_dotenv
load_dotenv()

# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


agent=Agent(
    model=Groq(id="qwen-qwq-32b"),
    description="Answer according to the asked Question/s",
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("What is the current tariff war bw US and CHina?")  