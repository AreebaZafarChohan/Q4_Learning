# 🧠 Prompt Exercise Agent System

This project demonstrates how to build an agent-based system using LLMs and custom tool functions to perform specific real-world tasks such as checking weather, finding restaurants, sending emails, scheduling meetings, and searching for products.

---

## 📋 Prompt Exercises and Intent Extraction

Below are the prompts, their extracted **intent**, and corresponding **parameters**:

### 🟩 Exercise 1: Weather Forecast

**Prompt:**  
> "What's the weather going to be like in Dubai tomorrow afternoon?"

- **Intent:** `get_weather_forecast`
- **Parameters:**
  - `location`: `"Dubai"`
  - `datetime`: `"tomorrow afternoon"`

---

### 🟨 Exercise 2: Restaurant Finder

**Prompt:**  
> "Find me some good Chinese restaurants near downtown that are open right now"

- **Intent:** `find_restaurants`
- **Parameters:**
  - `cuisine`: `"Chinese"`
  - `location`: `"near downtown"`
  - `open_now`: `True`

---

### 🟦 Exercise 3: Send Email

**Prompt:**  
> "Send an email to Sarah about the project deadline being moved to next Wednesday"

- **Intent:** `send_email`
- **Parameters:**
  - `recipient`: `"Sarah"`
  - `subject`: `"Project Deadline Update"`
  - `body`: `"The deadline has been moved to next Wednesday."`

---

### 🟧 Exercise 4: Meeting Scheduler

**Prompt:**  
> "Schedule a meeting with the marketing team for this Friday at 2 PM about the new campaign"

- **Intent:** `schedule_meeting`
- **Parameters:**
  - `participants`: `"marketing team"`
  - `datetime`: `"this Friday at 2 PM"`
  - `topic`: `"new campaign"`

---

### 🟥 Exercise 5: Product Search

**Prompt:**  
> "I want to buy wireless Bluetooth headphones under $100 with good reviews"

- **Intent:** `search_product`
- **Parameters:**
  - `product`: `"wireless Bluetooth headphones"`
  - `max_price`: `100`
  - `min_rating`: `4.0` (interpreting "good reviews")

---

## 🔧 Tools / Function Tool Implementation

Here's a sample `function_tool` implementation for product search:

```python
@function_tool
async def search_product(product: str, max_price: float, min_rating: float) -> List[str]:
    """
    Search for a product under a budget with a minimum rating.

    Args:
        product (str): Product name
        max_price (float): Max price in $
        min_rating (float): Minimum rating (e.g., 4.0)

    Returns:
        List[str]: Matching product titles
    """
    return [
        f"{product} - $89 - 4.5⭐",
        f"{product} - $75 - 4.6⭐"
    ]
```

---

## 🧪 Agent Configuration and Execution

```python
agent = Agent(
    name="Product Finder Agent",
    instructions="You are a product finder agent. Always call `search_product` tool when the user asks for help finding or buying a product.",
    tools=[search_product]
)

result = await Runner.run(
    agent,
    "I want to buy wireless Bluetooth headphones under $100 with good reviews",
    run_config=config
)
```

---

## 📤 Accessing Function Tool Response
After executing the agent with `Runner.run`, the tool result can be accessed via:

```python
print(result.final_output)        # Final message to the user
print(result.new_items)           # 🧃 New memory or items added during the run (optional depending on framework)
print(result.raw_responses)       # Raw LLM + tool responses
```

---

## 📚 Concepts Practiced

- Prompt Understanding and Intent Extraction
- Tool Function Design with Docstrings
- Agent-Based Execution Flow
- Async Programming with OpenAI/Gemini Models
- Using @function_tool decorator
- Accessing and printing tool responses

## ✅ Outcome

By completing these exercises, you’ve practiced:

- Creating intelligent agents
- Mapping natural language to structured function calls
- Integrating tools with LLMs
- Writing clean and understandable Python code for agent workflows

---

Built with ❤️ by **Areeba Zafar**

