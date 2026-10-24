import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path(__file__).with_name(".env"))

from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain.tools import tool
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch


llm=ChatGroq(temperature=0,model='openai/gpt-oss-120b')
tools=[TavilySearch()]
agent=create_agent(model=llm,tools=tools)

def main():
    print("Hello")
    result=agent.invoke({"messages":HumanMessage(content=("Search for 3 job postings for an ai engineer using langchain which is remote from canada from linkedin and list their details"))})
    print(result)

if __name__=='__main__':
    main()