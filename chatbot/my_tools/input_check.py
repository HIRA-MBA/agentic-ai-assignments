from agents import Agent, RunContextWrapper, Runner,RunContextWrapper
from agents.guardrail import input_guardrail, GuardrailFunctionOutput
from pydantic import BaseModel
#from my_agents.my_agents import chatBot

class Userinputcheck(BaseModel):
    is_negative_sentiment: bool
    reason: str

sentiment_detector = Agent(
    name="SentimentDetector",
    instructions="Determine whether user input is negative or offensive contains any bad comments .",
    output_type=Userinputcheck
)

@input_guardrail
async def check_negative(ctx:RunContextWrapper, agent:Agent, input:str)->GuardrailFunctionOutput:
    res = await Runner.run(sentiment_detector, input, context=ctx.context)

   
    return GuardrailFunctionOutput(output_info=res.final_output, 
    tripwire_triggered=res.final_output.is_negative_sentiment)
 