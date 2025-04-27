from agno.agent import Agent
from agno.models.groq import Groq 
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools 
# from agno.models.openai import OpenAIChat


import os
from dotenv import load_dotenv
load_dotenv()

# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

web_agent = Agent(
    name = "Web Agent",
    role = "Search the web for information",
    model = Groq(id = "qwen-qwq-32b"),
    tools = [DuckDuckGoTools()],
    instructions = "Always include sources",
    show_tool_calls = True,
    markdown = True,
)

finance_agent = Agent(
    name = "Finance Agent",
    role = "Get Stock Price Information",
    model = Groq(id = "qwen-qwq-32b"),    
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions = "Use comparisons to display data",
    show_tool_calls = True,
    markdown = True,
)

agent_team = Agent(
    team = [web_agent, finance_agent],
    model = Groq(id = "qwen-qwq-32b"),
    instructions = ["Provide a single, consolidated analysis", "Structure the response in this order only once:",
        "1. Data comparison",
        "2. Analysis",
        "3. Final recommendation"],
    show_tool_calls = True,
    markdown = True,
) 

agent_team.print_response("Analyze Stocks: NVDIA & GOOGLE, and suggest which to buy")