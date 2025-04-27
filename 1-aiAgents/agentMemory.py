from agno.agent import Agent
from agno.models.groq import Groq 
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
# from agno.models.openai import OpenAIChat
# from agno.embedder.openai import OpenAIEmbedder
# from agno.vectordb.lancedb import LanceDb, SearchType

import os
from dotenv import load_dotenv
load_dotenv()

# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

#  no embedder (no memory) because openai quota reached

agent = Agent( 
#    model = OpenAIChat(id = "gpt-4-1106-preview"),
    model = Groq(id = "qwen-qwq-32b"),    
    description="You are a Goldfish expert",
    instructions=[
        "Search your knowledge base for Goldfish care.",
        "If the PDF does not contain enough knowledge material, search the web to answer the question.",
        "Prefer the knowledge in the PDF over the web."
    ],
    knowledge=PDFUrlKnowledgeBase(
    urls=["https://petadvocacy.org/wp-content/uploads/2022/01/Goldfish-Care-Sheet.pdf"]),
    tools = [DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

if agent.knowledge is not None:
    agent.knowledge.load()

agent.print_response("How to carefully put goldfish in a new tank?")    