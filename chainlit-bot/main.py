import chainlit as cl
from agents import Runner,set_tracing_disabled
from my_agent.my_agent import general_agent



set_tracing_disabled(True)


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("history", [])  # memory
    await cl.Message("Hello, I am your assistant.").send()

@cl.on_message
async def on_message(message: cl.Message):
    # Show "searching..."
    msg = await cl.Message("Searching...").send()

    # Get history and add new user question
    history = cl.user_session.get("history")
    history.append(message.content)

    # Run agent with history as context
    result = Runner.run_sync(general_agent, input="\n".join(history))

    # Update message with final 
    
    msg.content = result.final_output
    await msg.update()
    

    # Save answer into history
    history.append(result.final_output)
    cl.user_session.set("history", history)
