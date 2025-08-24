from agents import Runner,set_tracing_disabled
from my_agent.my_agent import math_agent

set_tracing_disabled(True)
prompt=input("Enter your qustion  => ")
 
result =Runner.run_sync(math_agent,prompt)

print(result.final_output)
