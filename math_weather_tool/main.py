from agents import RunConfig, Runner,set_tracing_disabled
from my_agent.my_agent import my_assistant
from my_config.my_config import model

set_tracing_disabled(True)
prompt=input("Enter your question  =>  ")


result=Runner.run_sync(my_assistant,prompt,run_config=RunConfig(model=model))
print(result.final_output)
