# Exercise 3: Send an email to Sarah about the project deadline being moved to next Wednesday

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
    model_provider=external_client, # type: ignore
    tracing_disabled=True,
)

@function_tool
async def send_email(recipient: str, subject: str, body: str) -> str:
    """
    Send an email with the specified content.
    
    Args:
        recipient (str): Recipient's name or email
        subject (str): Email subject
        body (str): Email body
    
    Returns:
        str: Status message
    """
    return f"Email sent to {recipient} with subject '{subject}' and body '{body}'"


async def main():
    
    agent = Agent(
        name="Email Sender Agent",
        instructions="You are an email sender agent. Always call the `send_email` tool when asked to send an email.",
        tools=[send_email]
    )

    result = await Runner.run(
        agent,
        "Send an email to Sarah about the project deadline being moved to next Wednesday",
        run_config=config
    )
    print(result.final_output)
    print("\n====================================\n")
    print(result.raw_responses)
    print("\n====================================\n")
    print(result.new_items)


if __name__ == "__main__":
    asyncio.run(main())
