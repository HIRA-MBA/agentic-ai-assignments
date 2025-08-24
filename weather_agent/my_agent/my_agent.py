from agents import Agent, ModelSettings
from my_config.my_config import Model
from my_tool.weather_api_tool import get_weather
from agent_hooks.agent_hook import MyAgentHooks


weather_agent=Agent(name="Weather_assiatant",
                instructions='''
                  You are a helpful assistant.
        When the user asks about weather, ALWAYS call the get_weather tool
        with the city name EXACTLY as the user typed it.
        Do not replace it, do not guess, do not rephrase.
                ''',
                tools=[get_weather],
                model_settings=ModelSettings(tool_choice="required"),
                
                hooks=MyAgentHooks(),
                model=Model)