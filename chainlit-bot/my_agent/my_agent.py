from agents import Agent
from my_config.my_config import model


general_agent=Agent(name="Assistant",
                    instructions="you are a helpful assitant, give a brief answer to the query asked",
                    model=model)