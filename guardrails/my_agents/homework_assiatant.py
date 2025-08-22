from agents import Agent
from my_config.my_config import Model
from guardrail_function.guardrail_function import input_guardrail_function,output_guardrail_function

homework_assistant = Agent(
    name="Homework Assistant",
    instructions="""
    You are helpful homework assistant. help the student in doing assignments other than maths.""",
    model=Model,
    input_guardrails=[input_guardrail_function],
    output_guardrails=[output_guardrail_function]
    
)