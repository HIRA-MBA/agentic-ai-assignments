from agents import Runner,set_tracing_disabled
from my_agent.my_agent import general_assistant
import asyncio


set_tracing_disabled(True)

async def main():
    print(f' Welcome to TrendWear Clothing')

    prompt=input("what do you want to Know  ")

    result=await Runner.run(general_assistant,input=prompt)

    print(result.final_output)

asyncio.run(main())
