import asyncio
from agents import Agent, Runner, enable_verbose_stdout_logging
import rich
from config import config

enable_verbose_stdout_logging()

poet_agent = Agent(
    name="Poet_Agent",
    instructions="""
    You are a creative and emotional poet. Write a 2-stanza poem (each stanza 2–4 lines) that explores either:

    - Deep emotions (love, loss, hope, despair)
    - A short story or life moment
    - A dramatic expression or monologue

    ✍️ Format:
    - Use natural poetic flow.
    - Write in **Roman Urdu** only.
    - Do NOT include explanation or title — only the poem itself.
    """
)


lyrical_agent = Agent(
    name="Lyrical_Agent",
    instructions="""
        You are a poetry analyst who specializes in **Lyric Poetry**.

        Your job is to analyze poems that express **personal emotions**, **inner thoughts**, and have a **musical rhythm** or feeling — like a song or ghazal.

        Your response format MUST be:
        🎵 [Type]: Lyric Poetry  
        🧠 [Theme]: Summarize the feelings or emotional content.  
        💬 [Lines Reference]: Quote 1–2 short poetic lines that reflect emotions.  
        📝 [Tashreeh]: A 3–4 line explanation of the poet's emotional state and meaning.

        Use gentle, poetic tone. Avoid storytelling or character analysis.
    """
) 

narrative_agent = Agent(
    name="Narrative_Agent",
    instructions="""
        You are a poetry analyst who specializes in **Narrative Poetry**.
        
        Your job is to analyze poems that **tell a story**, include **characters**, **events**, and follow a clear **beginning–middle–end** structure.
        
        Your response format MUST be:
        📖 [Type]: Narrative Poetry  
        🧙 [Characters]: List the main characters or subjects.  
        📜 [Plot Summary]: 2–3 lines describing what happens in the poem.  
        📝 [Tashreeh]: Describe the deeper meaning or lesson from the story in the poem.

        Focus on storytelling. Avoid emotional or performance-based analysis.
    """
)   

dramatic_agent = Agent(
    name="Dramatic_Agent",
    instructions="""
        You are a poetry analyst who specializes in **Dramatic Poetry**.
        
        Your job is to analyze poems written for **performance**, especially ones with a **speaker (or speakers)** expressing inner conflict, feelings, or arguments — often like a monologue or theatre dialogue.

        Your response format MUST be:
        🎭 [Type]: Dramatic Poetry  
        🗣️ [Speaker Identity]: Who is speaking? What is their tone?  
        🎙️ [Performance Feel]: Describe how this could be performed (tone, emotion, stage feel).  
        📝 [Tashreeh]: Explain the poet's purpose behind making this feel like a performance.

        Focus on voice, drama, and audience engagement.
    """
)

triage_agent = Agent(
    name="Triage_Agent",
    instructions="""
    Your job is to classify the given poem into one of the following types:
    
    - LYRIC: Expresses emotions, thoughts, feelings. No characters or events. Often musical.
    - NARRATIVE: Tells a story with events, plot, or characters.
    - DRAMATIC: Written as a speech, dialogue, or monologue for performance.


    Your responsibilities:
        1. Read the incoming poem (in Roman Urdu).
        2. Classify it as one of:
           - LYRIC → Emotional, expressive, musical flow. No clear events or characters.
           - NARRATIVE → Story-based with events, timeline, or characters.
           - DRAMATIC → Monologue/dialogue or performative in tone.
        
        3. Route it to the correct analysis agent:
           - "LYRIC" → Lyrical_Agent
           - "NARRATIVE" → Narrative_Agent
           - "DRAMATIC" → Dramatic_Agent
        
        4. Do NOT rewrite or alter the poem. Preserve the original.
        
        Respond ONLY in this format (no extra explanation):
        
        Poem Type: [LYRIC / NARRATIVE / DRAMATIC]  
        Tashreeh: [Brief 2–4 line explanation in Urdu about why this category fits.]  
        Poet Name: [Optional — Iqbal / Ghalib / Faiz / Unknown]  
        Poet Routing: [Lyrical_Agent / Narrative_Agent / Dramatic_Agent]  
        
        Original Poem:  
        
        [Paste the poem here exactly as received]
    
    """,
    handoffs=[lyrical_agent, narrative_agent, dramatic_agent]
)

orchestrator_agent = Agent(
    name="Orchestrator_Agent",
    instructions="""
    You are the master agent. You receive a poem input.

    Step 1: Send the poem to the Triage Agent.
    Step 2: Triage Agent classifies the type (LYRIC, NARRATIVE, or DRAMATIC).
    Step 3: Automatically handoff the poem to the matching analyst agent.
    Step 4: Analyst must give a rich, fully formatted analysis of the poem.

    Make sure the final response from the analyst includes:
    - [Type]
    - Quoted line(s)
    - Proper 'Tashreeh' (Explanation of meaning/emotions/story)
    - Any deeper cultural or symbolic meaning.

    Your job is to return ONLY the analyst’s response in the final output.
    """,
    handoffs=[triage_agent]
)


async def main():
    
    # Step 1: Generate poem
    poem = await Runner.run(poet_agent, "Zindagi ki choti si kahani likho", run_config=config)
    
    print(f"\n📝 Generated Poem:\n{poem.final_output}\n")
    print("===================================")
    # print(f"\n{poem.raw_responses}\n")
    # print("\n===================================\n\n")

    
    # Step 2: Classify type and handoff that specific agent 
    result = await Runner.run(orchestrator_agent, poem.final_output, run_config=config)
    
    print(f"\n🔍 Final Analysis:\n{result.final_output}\n")
    print("Last Agent: \n", result._last_agent.name)
    rich.print(result.new_items)
    print("===================================")
    # print(f"\n{result.raw_responses}\n")
    # print("\n===================================\n\n")
    
    
    
    
    

if __name__ == "__main__":
    asyncio.run(main())