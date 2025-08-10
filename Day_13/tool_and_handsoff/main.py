from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging
from config import config
import rich

# enable_verbose_stdout_logging()


@function_tool
async def get_location() -> str:
    # """
    # Retrieves the user's location.

    # Args:
    #     location (str): The location provided by the user.

    # Returns:
    #     str: A string indicating the user's current location. 
    #          If no location is provided, defaults to 'Karachi'.    
    # """
    return f"I am currently in my home."

@function_tool
async def get_breaking_news() -> str:
    # """
    # Retrieves the breaking news based on the given time.

    # Args:
    #     time (str): The time for which to fetch breaking news. Defaults to current time if not provided.

    # Returns:
    #     str: A string containing the breaking news summary based on provided filters.
    # """
    return f"There is no any kind of breaking news now."

botany_agent = Agent(
    name="Botany_Agent",
    instructions="You are a plant specialist. Your job is to provide accurate yet concise information or summary about plants, including their classification, benefits, care tips, and environmental needs. Answer all questions like a botany expert."
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
    handoffs=[botany_agent]
)

result = Runner.run_sync(
    agent,
    """
    1. What is my current location?
    2. Any breaking news?
    3. What is photosynthesis?
    """,
    run_config=config
)

print("\n",'='*50)
rich.print(result.new_items)

print('='*50)
print("Result: ", result.last_agent.name)
print("Final Output: ", result.final_output)
