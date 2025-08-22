
from agents import Agent,ModelSettings
from my_config.my_config import Model
from my_hooks.my_hooks import MyHooks
from tools.my_tools import tavily_search


        

research_agent = Agent(
    name="ResearchAgent",
    instructions="You are a research assistant. Use Tavily for live web search.",
    model_settings=ModelSettings(tool_choice="required"),
    hooks=MyHooks(),
    tools=[tavily_search], 
  
    model=Model 
    
)