from agents import RunConfig, Runner,set_tracing_disabled,SQLiteSession
from my_agents.my_agents import TriageAgent  # Import  agents

import asyncio
from my_config.my_config import Model

#setting openai tracing disable

set_tracing_disabled(True)




async def main():
    # Create persistent session
    my_session = SQLiteSession("mysession_123", "my_conversation.db")

    #  Initial greeting
    print(" Welcome to TrendyWear! I’m your shopping assistant.")
    print("I can help you with FAQs, track orders, or connect you to a human if needed.")
    print("Type 'exit' anytime to leave the chat.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print(" Thank you for visiting TrendyWear. Have a great day!")
            break

        # Run agent with memory (session)
        result = await Runner.run(
            starting_agent=TriageAgent,
            input=user_input,
            session=my_session,
            run_config=RunConfig(model=Model)
        )

        #  Show chatbot response
        print(f" TrendyBot: {result.final_output}\n")


if __name__ == "__main__":
    asyncio.run(main())
