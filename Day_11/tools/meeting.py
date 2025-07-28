# Exercise 4: Schedule a meeting with the marketing team for this Friday at 2 PM about the new campaign

import asyncio
from agents import Agent, Runner, RunConfig, function_tool, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI API KEY is not set. Please ensure that it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,  # type: ignore
    tracing_disabled=True,
)

@function_tool
async def schedule_meeting(participants: str, datetime: str, topic: str) -> str:
    """
    Schedules a meeting with participants at a given time.

    Args:
        participants (str): Team or individuals
        datetime (str): Meeting time
        topic (str): Meeting topic

    Returns:
        str: Confirmation
    """
    return f"📅 Meeting with {participants} scheduled for {datetime} to discuss '{topic}'."

async def main():
    agent = Agent(
        name="Schedule Meeting Agent",
        instructions="You are a meeting scheduling agent. Always call the `schedule_meeting` tool when the user talks about scheduling a meeting.",
        tools=[schedule_meeting]
    )

    result = await Runner.run(
        agent,
        "Schedule a meeting with the marketing team for this Friday at 2 PM about the new campaign",
        run_config=config
    )
    print(result.final_output)
    print("\n====================================\n")
    print(result.raw_responses)
    print("\n====================================\n")
    print(result.new_items)

if __name__ == "__main__":
    asyncio.run(main())
