import chainlit as cl
from agents import Runner,set_tracing_disabled
from my_agent.my_agent import weather_agent  # import your Agent


set_tracing_disabled(True)
@cl.on_chat_start
async def start():
    await cl.Message(content=" Hello! I’m your Weather Assistant Bot.").send()
    await cl.Message(content=" Please enter a city name to get the weather.").send()

@cl.on_message
async def main(message: cl.Message):
    city = message.content.strip()

    # Show searching status
    msg = cl.Message(content=f"🔎 Searching weather for **{city}**...")
    await msg.send()

    # Run the agent
    result = await Runner.run(starting_agent=weather_agent, input=city)

    # Only show final answer
    msg.content = f"📍 Weather update for **{city}**:\n\n{result.final_output}"
    await msg.update()
