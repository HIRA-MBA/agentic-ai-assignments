from agents import set_tracing_disabled,Runner
from my_agent.my_agent import booking_agent
from dynamic_instructions.dynamic_instructions import UserName
import asyncio


set_tracing_disabled(True)

async def main():
    """Main entry point for hotel booking assistant."""

    print("Welcome to the Hotel Booking Assistant")
    user_name = input("Please enter your name: ").strip()
    query = input("What would you like to ask? ").strip()

    try:
        # Run agent asynchronously
        result = await Runner.run(
            starting_agent=booking_agent,
            input=query,
            context=UserName(name=user_name, query=query),
        )

        print("\n✅ Booking Agent Response:")
        print(result.final_output)

    except Exception as e:
        print("\n❌ An error occurred:", str(e))



asyncio.run(main())
