# In this example, we'll explore what happens when we have two tools and two handoffs in a single prompt — how will the LLM respond?

import asyncio
from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging
from config import config
import rich

# enable_verbose_stdout_logging()


@function_tool
def get_location() -> str:
    return f"I am currently in my home."

@function_tool
def get_breaking_news() -> str:
    return f"There is no any kind of breaking news now."

botany_agent = Agent(
    name="Botany_Agent",
    instructions="You are a plant specialist. Your job is to provide accurate yet concise information or summary about plants, including their classification, benefits, care tips, and environmental needs. Answer all questions like a botany expert."
)

medicine_agent = Agent(
    name="Medicine_Agent",
    instructions = "You are a medicine specialist. Your job is to provide accurate yet concise information or summaries about medicine including their formulas and usage."
)


agent = Agent(
    name="Assistant",
    instructions="""
    You are a helpful assistant. You MUST use your tools if the user asks about location or breaking news.
    Use:
    - `get_location()` for location queries.
    - `get_breaking_news()` for news queries.
    You can also pass plant-related questions to the botany agent.
    """,
    tools=[get_location, get_breaking_news],
    handoffs=[botany_agent, medicine_agent]
)

async def main():
    result = await Runner.run(
    agent,
    """
    1. What is my current location?
    2. Any breaking news?
    3. Tell me about panadol medicine?
    4. What is photosynthesis?

    """,
    run_config=config
    
    )
    
    

    print("\n",'='*50)
    rich.print(result.new_items)

    print('='*50)
    print("Result: ", result.last_agent.name)
    print("Final Output: ", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())    
