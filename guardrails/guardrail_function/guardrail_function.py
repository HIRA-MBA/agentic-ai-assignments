from agents import input_guardrail,output_guardrail,RunContextWrapper,Agent,Runner,GuardrailFunctionOutput
from my_agents.input_guardrail_agent import input_guardrail_agent
from my_agents.output_guardrail_agent import output_guardrail_agent

@input_guardrail
async def input_guardrail_function(ctx:RunContextWrapper,agent:Agent,input):
    result=await Runner.run(input_guardrail_agent,context=ctx.context,input=input)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_question_realted_to_Maths
    )

@output_guardrail
async def output_guardrail_function(ctx:RunContextWrapper,agent:Agent,input):
    result=await Runner.run(output_guardrail_agent,context=ctx.context,input=input)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_question_realted_to_politics
    )