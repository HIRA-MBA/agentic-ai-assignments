from agents import Runner,InputGuardrailTripwireTriggered,OutputGuardrailTripwireTriggered,set_tracing_disabled
from my_agents.homework_assiatant import homework_assistant

set_tracing_disabled(True)


prompt=input("Enter your question here --> ")
try:

    res = Runner.run_sync(
        starting_agent=homework_assistant, 
        input=prompt,
    )

    print(res.final_output)
except InputGuardrailTripwireTriggered as e:
    print(e)

except OutputGuardrailTripwireTriggered as e:
    print(e)
