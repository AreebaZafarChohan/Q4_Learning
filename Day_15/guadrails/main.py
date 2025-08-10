import asyncio
from agents import Agent, GuardrailFunctionOutput, InputGuardrailTripwireTriggered, Runner, TResponseInputItem , enable_verbose_stdout_logging, input_guardrail
from pydantic import BaseModel
from config import run_config

class Management(BaseModel):
    reasoning: str
    is_tuesday_slot: bool

management_agent: Agent = Agent(
    name="Management_Agent",
    instructions="""
    You are a management agent that changes the slot timings of students if they are saying to change. But tuesday class seats are full so if any student want to change their slot in tuesday so you are denied to change slot.
    """,
    output_type=Management
)

@input_guardrail
async def management_guadrail(ctx, agent: Agent, input: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:
    result = await Runner.run(management_agent, input, run_config=run_config)
    print("Management agent output:", result.final_output)

    # Safety check in case LLM response isn't parsed correctly
    if isinstance(input, str) and "tuesday" in input.lower():
        is_tuesday = True
    else:
        is_tuesday = bool(result.final_output.is_tuesday_slot)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=is_tuesday
    )

    
teacher_agent: Agent = Agent(
    name="Teacher_Agent",
    instructions="""You are a teacher agent. Your task is to listen user query and if they say about time change of slots so check that it is tuesday or not.""",
    input_guardrails=[management_guadrail],
)    

async def main():
    try:
        print("\n--- TEST 1: Requesting Sunday Slot ---")
        result1 = await Runner.run(teacher_agent, "I want to change my friday slot into sunday slot", run_config=run_config)
        print("Result:", result1)
        print("\nFinal Output:", result1.final_output)
        print("Input Guardrail didn't trip — correct behavior.")

        print("\n","="*50, "\n")

        print("\n--- TEST 2: Requesting Tuesday Slot ---")
        result2 = await Runner.run(teacher_agent, "I want to change my friday slot into tuesday slot", run_config=run_config)
        print("Result:", result2)
        print("\nFinal Output:", result2.final_output)
        print("Input Guardrail NOT triggered — This should NOT happen!")  # should not print

    except InputGuardrailTripwireTriggered:
        print("🚫 You can't change your slot to Tuesday — seats are full.")

        
if __name__ == "__main__":
    asyncio.run(main())            