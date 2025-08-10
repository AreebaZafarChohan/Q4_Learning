# 🎭 Poetry Analysis System

A multi-agent system that classifies poetry into **Lyric**, **Narrative**, or **Dramatic** and provides a detailed analysis.

## 🛠 How It Works
1. **Poet Agent** — Receives a poem as input.
2. **Triage Agent** — Determines the poetry type based on clues:
   - **Lyric**: Personal emotions, musical quality.
   - **Narrative**: Storytelling, characters, plot.
   - **Dramatic**: Performance-focused, monologue/dialogue.
3. **Specialist Analyst Agents** — Provide in-depth analysis for their assigned type.
4. **Parent Orchestrator Agent** — Routes the poem from triage to the correct analyst and returns the final formatted output.

---

## 📜 Example
**Input Poem:**
*The broken wing of my desire*
*Shall never soar in skies of fire,*
*But like a wounded bird shall rest*
*In the still waters of thy breast.*


**Detected Type:** `Lyric Poetry`  
**Analysis:**  
- **Theme**: Unfulfilled love  
- **Techniques**: Metaphor, imagery  
- **Era**: Early 20th century Indian poetry  
- **Interpretation**: A metaphorical depiction of restrained desire, evoking limitation and solace.

---

## 🚀 Running the Program
```bash
uv run main.py
```
---

## 📌 Features

**🎯 Accurate classification of poetry type.**
**🧠 Detailed thematic and stylistic analysis.**
**🎨 Rich console UI with color-coded panels.**

**👨‍💻 Developed by** *Areeba Zafar*