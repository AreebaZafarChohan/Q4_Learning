# Exercise 1: What's the weather going to be like in Dubai tomorrow afternoon?

import asyncio
from agents import Agent, Runner, RunConfig, function_tool, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
import requests

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
async def get_weather(location: str, time: str) -> str:
    """
    Get the weather forecast for a specific location and time.
    
    Args:
        location (str): The name of the location to get the weather for.
        time (str): The time of the location to get the weather for. (Note: Not used in API but included for prompt clarity)
        
    Returns:
        str: A brief description of the weather forecast.
    """
    try:
        api_key = os.getenv("OPENWEATHER_API_KEY")
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        params = {
            "q": location,
            "appid": api_key,
            "units": "metric"
        }
        
        res = requests.get(base_url, params=params)
        data = res.json()
        
        if res.status_code != 200 or 'weather' not in data:
                return f"Sorry, unable to fetch weather for {location}."
        
        weather_desc = data["weather"][0]["description"] 
        temp = data["main"]["temp"]
        
        return f"The weather in {location} {time} is {weather_desc} with temperature around {temp}°C."
    
    except Exception as e:
        return f"Error occurred: {str(e)}"
   


async def main():
    
    agent = Agent(
        name="Weather Agent",
        instructions="You are a weather agent. Always call tool for weather",
        tools=[get_weather]
    )

    result = await Runner.run(
        agent,
        "What's the weather going to be like in Dubai tomorrow afternoon?",
        run_config=config
    )
    print(result.final_output)
    print("\n====================================\n")
    print(result.raw_responses)
    print("\n====================================\n")
    print(result.new_items)


if __name__ == "__main__":
    asyncio.run(main())
