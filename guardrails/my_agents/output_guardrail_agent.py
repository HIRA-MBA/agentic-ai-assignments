from agents import Agent
from my_config.my_config import Model
from dataclass.dataclass import Output_Guardrail

output_guardrail_agent=Agent(name="output_guardrail_agent",
                        instructions='''you are output guardrail agent,
                         that will check the query should not related with political event or personality''',
                        model=Model,output_type=Output_Guardrail)
