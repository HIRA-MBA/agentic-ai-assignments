from agents import Agent
from my_config.my_config import Model
from dataclass.dataclass import Input_Guardrail


input_guardrail_agent=Agent(name="input_guardrail_agent",
                        instructions="you are input guardrail agent, that will check the query should not related with math",
                        model=Model,output_type=Input_Guardrail)