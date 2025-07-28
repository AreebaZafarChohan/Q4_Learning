# Exercise 5: I want to buy wireless Bluetooth headphones under $100 with good reviews

import asyncio
from typing import List
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
async def search_product(product: str, max_price: float, min_rating: float) -> List[str]:
    """
    Simulates product search by returning a list of demo products matching the user's criteria.

    Args:
        product (str): Product name or type
        max_price (float): Maximum acceptable price in USD
        min_rating (float): Minimum acceptable rating

    Returns:
        List[str]: List of matching product details
    """

    # 🔧 Mock product catalog
    demo_products = [
        {"name": "Anker Soundcore Life Q20", "price": 59.99, "rating": 4.5},
        {"name": "JBL Tune 510BT", "price": 49.95, "rating": 4.3},
        {"name": "Sony WH-CH520", "price": 58.00, "rating": 4.4},
        {"name": "TOZO HT2 Hybrid ANC", "price": 69.99, "rating": 4.6},
        {"name": "ZIHNIC Foldable Wireless Headphones", "price": 29.99, "rating": 4.1},
        {"name": "Beats Flex Wireless Earbuds", "price": 69.95, "rating": 4.0},
        {"name": "SoundPEATS Air3 Deluxe HS", "price": 39.99, "rating": 4.4},
        {"name": "Tribit XFree Go", "price": 32.99, "rating": 4.2},
    ]

    # 🧠 Filter by price and rating
    matching = [
        f"{p['name']} - ${p['price']} - {p['rating']}⭐"
        for p in demo_products
        if p['price'] <= max_price and p['rating'] >= min_rating
    ]

    if not matching:
        return [f"No {product} found under ${max_price} with {min_rating}+⭐ rating."]

    return matching

async def main():
    
    agent = Agent(
        name="Product Finder Agent ",
        instructions="You are a product finder agent. Always call `search_product` tool when the user asks for help finding or buying a product.",
        tools=[search_product]
    )

    result = await Runner.run(
        agent,
        "I want to buy wireless Bluetooth headphones under $100 with good reviews",
        run_config=config
    )
    print(result.final_output)
    print("\n====================================\n")
    print(result.raw_responses)
    print("\n====================================\n")
    print(result.new_items)


if __name__ == "__main__":
    asyncio.run(main())
