# Exercise 2: Find me some good Chinese restaurants near downtown that are open right now

import asyncio
from typing import List
from agents import Agent, Runner, RunConfig, function_tool, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import aiohttp
from datetime import datetime

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
google_places_api_key = os.getenv("GOOGLE_PLACES_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI API KEY is not set. Please ensure it is defined in your .env file.")

if not google_places_api_key:
    raise ValueError("GOOGLE_PLACES_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
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
async def find_restaurants(cuisine: str, location: str, open_now: bool) -> str:
    """
    Simulates finding restaurants for demonstration without calling real APIs.
    
    Args:
        cuisine (str): Type of food
        location (str): City or area
        open_now (bool): Whether to find only currently open places
    
    Returns:
        str: Fake list of restaurants for demo purposes
    """
    # Fake dataset
    fake_restaurants = [
        {"name": "Golden Dragon", "address": f"123 Main St, {location}", "open": True},
        {"name": "Panda Express", "address": f"456 Lakeview Rd, {location}", "open": True},
        {"name": "Red Wok", "address": f"789 Hilltop Ave, {location}", "open": False},
        {"name": "Chopsticks Delight", "address": f"321 Sunset Blvd, {location}", "open": True},
        {"name": "Beijing Bites", "address": f"654 Garden St, {location}", "open": False},
    ]

    # Filter based on `open_now`
    filtered = [
        r for r in fake_restaurants
        if not open_now or r["open"]
    ]

    if not filtered:
        return f"No {cuisine} restaurants found in {location} that are open right now."

    response = f"🍽️ Top {cuisine} restaurants in {location}:\n\n"
    for i, r in enumerate(filtered, 1):
        status = "🟢 Open Now" if r["open"] else "🔴 Closed"
        response += f"{i}. {r['name']}\n   📍 {r['address']}\n   {status}\n\n"

    return response.strip()

async def main():
    agent = Agent(
        name="Restaurant Finder Demo Agent",
        instructions="You are a demo restaurant finder agent. Always use the `find_restaurants` tool to answer food or restaurant-related questions.",
        tools=[find_restaurants]
    )

    query = "Find me some good Chinese restaurants near downtown Karachi that are open right now."

    result = await Runner.run(
        agent,
        query,
        run_config=config
    )

    print(result.final_output)
    print("\n====================================\n")
    print(result.raw_responses)
    print("\n====================================\n")
    print(result.new_items)

if __name__ == "__main__":
    asyncio.run(main())