from agents import Agent
from dynamic_instructions.dynamic_instructions import UserName,dynamic_instructions
from my_config.my_config import Model

booking_agent=Agent[UserName](name="Reservation Agent",instructions=dynamic_instructions,model=Model)
