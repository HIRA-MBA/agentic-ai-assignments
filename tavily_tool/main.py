from agents import Runner,set_tracing_disabled
from my_agent.my_agent import research_agent


set_tracing_disabled(True)
prompt=input("Enter what do you want to search here ==>  ")
result=Runner.run_sync(research_agent,prompt)
print(result.final_output)
