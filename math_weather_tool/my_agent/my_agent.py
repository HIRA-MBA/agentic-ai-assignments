from agents import Agent, ModelSettings

from my_tools.math_tool import math_function
from my_tools.weather_tool import weather_tool
from my_hooks.my_hooks import Hooks
my_assistant=Agent(name="My_assiatnt",
                   instructions=""" you are helpful assiatant:
                   -you will either use addition tool  for addtion
                   - or weather tool when asked about weather of any city
                   -dont answer except that simply refuse
                    """,
                   tools=[math_function,weather_tool],
                   model_settings=ModelSettings(tool_choice="required"),
                   hooks=Hooks())
                   