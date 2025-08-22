from tavily import TavilyClient
from decouple import config
from agents import function_tool


tavily=TavilyClient(api_key=config("TAVILY_API_KEY"))

@function_tool
def tavily_search(query: str, max_results: int = 5):
    """Search the internet in real time for up-to-date information."""
    result = tavily.search(query=query, max_results=max_results)
    return result
