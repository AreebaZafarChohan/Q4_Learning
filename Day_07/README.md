# Task 07: OpenAI Agents SDK – Quick Summary

This task explores the structure and design of OpenAI's Agentic SDK, focusing on key components like `Agent`, `Runner`, and the use of generics.

---

## 🔍 Key Concepts

### 1. `@dataclass` for Agent
The `Agent` class is a dataclass to reduce boilerplate and make data handling clean and efficient.

### 2. Instructions as Field or Callable
- `instructions` define the system prompt.
- It can be a static string or a callable to generate dynamic context-based prompts.

### 3. User Prompt via `Runner.run()`
- The user prompt is passed to the `run()` method, which is a classmethod.
- This helps in running agents with different inputs and contexts.

### 4. Purpose of `Runner` Class
`Runner` manages agent execution, handling input, tools, context, and output generation.

### 5. Generics and `TContext`
Generics (`TypeVar`) enable flexible type-safe handling of different context structures.

---

## 📚 References

- [Agent Docs](https://openai.github.io/openai-agents-python/ref/agent/)
- [Runner Docs](https://openai.github.io/openai-agents-python/ref/run/)
- [Panaverse Repo](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first)

---

> ✨ Explore how agentic AI can dynamically interact with tools and contexts using a clean and modular SDK approach.
