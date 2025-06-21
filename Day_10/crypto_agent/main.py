"""
Goal: I want to get the current Market Rate of Crypto Currencies.

Breaking the problem into bullet Points:

1. Install Required Libraries
2. Create an agent named CryptoDataAgent.
3. Binance API: Utilize requests to fetch ticker information (tool calling)
4. Define the Agent's Workflow (Implement Runner.run)
5.. Execute the Agent  

"""

import os
from openai import AsyncOpenAI
from agents import Agent, RunConfig, Runner, OpenAIChatCompletionsModel, function_tool
from dotenv import load_dotenv
import requests

# load .env file 
load_dotenv()

# get gemini api key from .env file
gemini_api_key = os.getenv("GEMINI_API_KEY")

# check that if api key is set or not
if not gemini_api_key:
    raise ValueError("GEMINI API KEY is not set. Please ensure that API kEY is set in your .env file.")

# create external client 
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# create gemini model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)


# configure model and api
config = RunConfig(
    model=model,
    model_provider=external_client, # type: ignore
    tracing_disabled=True,
)

# create a get_crypto_price tool to get current price of symbol
@function_tool
def get_crypto_price(symbol: str) -> str:
    
    """
    Get the current market price of a crypto symbol from Binance.
    Example: BTCUSDT, ETHUSDT
    """
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"The current price of {symbol} is {data['price']} USDT."
        else:
            return f"API ERROR: Status code {response.status_code}"
    except Exception as e:
        return f"Exception occurred: {str(e)}" 

# Create an Agent 
agent: Agent = Agent(
    name="CryptoDataAgent",
    instructions="You are an expert crypto agent. Use the get_crypto_price tool to answer user's query about crypto market prices.",
    tools=[get_crypto_price]
)

# Run the agent
result = Runner.run_sync(
    agent,
    "What's the price of BTCUSDT?",
    run_config=config
)

print("\nCalling Crypto Data Agent\n")
print(result.final_output)

