from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv(override=True)

llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(model=llm, tools= tools)


def main():
    print("Hello from ai-job-hunt-agent!")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job posting for an AI engineer using Langchain in Bangalore on Linkedin and list their details")})
    print(result)


if __name__ == "__main__":
    main()
