from agents import Agent,ModelSettings
from my_config.my_config import Model
from tools.addition import addition
from tools.subtraction import subtraction
from hooks.agent_hooks import MyAgentHooks

math_agent=Agent(
    name="Math Assitant",
    instructions='''     You are a helpful math agent:
    - Only answer math related problems.
    - Always use tools for addition and subtraction and perform other operation directly.
    - Refuse politely if question is not about math.
    ''',
    model_settings=ModelSettings(tool_choice="auto"),
    tools=[addition,subtraction],
    hooks=MyAgentHooks(),
    model=Model
    
)