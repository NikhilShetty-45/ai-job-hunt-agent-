from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
#from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv(override=True)

""" 
tavily = TavilyClient()

@tool
def search(query: str) -> str:

    Tool that searches over the internet
    Args:
        query: The query to search for
    Returns:
        The search Result

    print(f"Searching for {query}")
    return tavily.search(query=query)

 """
llm = ChatOpenAI()
tools = [TavilySearch()] #tools = [search]
agent = create_agent(model=llm, tools= tools)


def main():
    print("Hello from ai-job-hunt-agent!")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job posting for an AI engineer using Langchain in Bangalore on Linkedin and list their details")})
    print(result)


if __name__ == "__main__":
    main()
