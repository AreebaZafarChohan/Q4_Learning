# 🧪 Multi-Agent Tool & Handoff Behavior Test

This project tests how the **OpenAI Agents SDK** handles:
- **Tool Execution Order** (e.g., `get_location`, `get_breaking_news`)
- **Agent Handoffs** (passing plant-related queries to a `Botany_Agent`)
- Whether multiple tools can run in a single execution before/after handoffs.

---

## 📂 Key Files

### `main.py`
- **Agents:**
  - `Assistant` → Main agent that uses:
    - `get_location()` → Returns current location.
    - `get_breaking_news()` → Returns breaking news.
    - Can hand off plant-related questions to `Botany_Agent`.
  - `Botany_Agent` → Plant specialist for botany-related queries.

- **Tools:**
  - `get_location`
  - `get_breaking_news`

- **Logic:**
  - Runs 3 mixed queries (location, news, botany) to test:
    - If tools run before handoff.
    - Whether more than one tool runs.
    - If botany queries go to `Botany_Agent`.

---

## ▶️ Expected Behavior

**Input Prompt:**
*1. What is my current location?*
*2. Any breaking news?*
*3. What is photosynthesis?*


**Expected Flow:**
1. `Assistant` runs `get_location()` tool.
2. `Assistant` runs `get_breaking_news()` tool.
3. Handoff to `Botany_Agent` for photosynthesis question.

**Expected Output:**
- All tools return responses.
- Handoff executes correctly.
- `result.new_items` shows each tool and agent step.
- `result.final_output` contains combined answers.

---

## 🛠 How to Run
```bash
uv run main.py
```

---

## 📌 Note
This test is for educational purposes only — designed to analyze tool execution vs. handoff sequencing in OpenAI’s Agents SDK.

**Created by:** *Areeba Zafar*
