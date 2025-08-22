from agents import Agent, ModelSettings
from my_tools.tools import faq_lookup_tool
from my_tools.order_id import  get_order_status
from my_tools.input_check import check_negative

#chat bot that will answer FAQ and order tracking
chatBot = Agent(
    name="chatBot",
    instructions=(''' you are chatbot that will answer frequently asked question and track order when asked.
        If a user asks to track an order but doesn't include an order ID, ask for id.       
    
        then using the tool get_order_status check the order status if it is a valid order number
      '''
    ),
    
    tools=[get_order_status, faq_lookup_tool],
  
    input_guardrails=[check_negative]
)

humanAgent = Agent(
    name="humanAgent",
    instructions="Handle escalated or complex or negative-sentiment queries as a human agent would.",
    
)

TriageAgent = Agent(
    name="TriageAgent",
       instructions="""
        You are a triage agent for TrendyWear.
        - If the query is about an order status or a frequently asked question, ALWAYS handoff to chatBot.
        - If the query shows negative sentiment or needs escalation, ALWAYS handoff to humanAgent.
        - You CANNOT use tools. Only route to the correct agent.
        - Example:
            User: "Track my order" → handoff to chatBot
            User: "This brand is bad" → handoff to humanAgent
    """,
    handoffs=[chatBot, humanAgent],
    handoff_description="FAQs + order → chatBot | Negative → humanAgent"
)
