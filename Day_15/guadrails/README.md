# Teacher Agent with Input Guardrail (Agents SDK + Gemini API)

## 📌 Objective
Create a **Teacher Agent** with an **Input Guardrail** that triggers when a student tries to change their class timing to **Tuesday** (because Tuesday class seats are full).

**Exercise Goal:**
When running the prompt:
    **I want to change my class timings 😭😭**


The `InputGuardrailTripwireTriggered` exception should be called, and the message  
`🚫 You can't change your slot to Tuesday — seats are full.` should appear in the logs.

---

## 🛠 Tech Stack
- **Python 3.11+**
- **[Agents SDK](https://github.com/openai/openai-agents-python)**
- **Gemini API (via OpenAI SDK)**
- **Pydantic v2**
- **dotenv** (for environment variables)

---

## 📂 Project Structure

Day_15/
- │
- ├── main.py # Main program with Teacher & Management agents
- ├── config.py # Configuration for Gemini API & RunConfig
- ├── .env # Environment variables
- ├── exercise.txt # Exercise requirements
- ├── pyproject.toml
- ├── .gitignore
- ├── .venv
- ├── .python-version
- ├── uv.lock
- └── README.md # This file


---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone <https://github.com/AreebaZafarChohan/Q4_Learning/Day_15/guadrails/>
cd Day_15
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
.venv\Scripts\activate       # Windows
```

### 3. Install dependencies

```bash
uv add openai-agents python-dotenv pydantic 
```

### 4. Add your Gemini API key
Create a .env file in the project root:

```ini
GEMINI_API_KEY=your_gemini_api_key_here
```

## 🖥 How It Works

### 1. Management Agent
- Receives the user’s request.
- Checks if they are asking to change their slot to **Tuesday**.
- Returns a `GuardrailFunctionOutput` with `tripwire_triggered=True` if Tuesday is detected.

### 2. Teacher Agent
- Uses the **Management Guardrail** as an `input_guardrail`.
- If the guardrail trips, raises `InputGuardrailTripwireTriggered`.

---

## ▶️ Running the Program
```bash
uv run main.py
```

---

## Example Output
```sql
--- TEST 1: Requesting Sunday Slot ---
Management agent output: reasoning='The slot change is permitted as it is not a request to change a slot to Tuesday, which is currently full.' is_tuesday_slot=False                                                                                                                                                          False
Result: RunResult:
- Last agent: Agent(name="Teacher_Agent", ...)
- Final output (str):
    I can help you with that! Just to confirm, you're asking to change a slot that currently takes place on Friday to a slot on Sunday?
- 1 new item(s)
- 1 raw response(s)
- 1 input guardrail result(s)
- 0 output guardrail result(s)
(See `RunResult` for more details)

Final Output: I can help you with that! Just to confirm, you're asking to change a slot that currently takes place on Friday to a slot on Sunday?

Input Guardrail didn't trip — correct behavior.

==================================================


--- TEST 2: Requesting Tuesday Slot ---
Management agent output: reasoning='Tuesday slots are full and therefore I cannot change your Friday slot to Tuesday.' is_tuesday_slot=False
🚫 You can't change your slot to Tuesday — seats are full.

```
---

## 🔍 Key Files

### `config.py`
Handles:
- Loading `.env` file
- Setting up Gemini API via `AsyncOpenAI`
- Creating `RunConfig` for Agents SDK

### `main.py`
Implements:
- `Management` Pydantic model
- `management_agent` and `teacher_agent`
- Guardrail logic to detect Tuesday slot requests
- Test runs for both safe and restricted cases

---

## ✅ Expected Behavior

| Input Prompt | Expected Result |
|--------------|----------------|
| `"I want to change my friday slot into sunday slot"` | Passes, guardrail **not triggered** |
| `"I want to change my friday slot into tuesday slot"` | **Triggers guardrail** and raises `InputGuardrailTripwireTriggered` |

---

## 📸 Tracing Screenshot
Below is a tracing view showing the guardrail trigger for Tuesday slot request:

![Tracing Screenshot](/screenshots/input_guardrail_tripwire.png)

## 📜 License
This project is for **educational purposes** only.

---

**👩‍💻 Developed by:** *Areeba Zafar*
