from decimal import Rounded
from enum import Enum
from agents import Agent, Runner
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.markdown import Markdown
from rich.box import ROUNDED, DOUBLE
from rich.table import Table
from rich.layout import Layout
from rich.text import Text
from poetry_data import POETRY_DATABASE
from config import config
import re

# Initialize console

console = Console()

# === Constants and Enums ===

class PoetryType(Enum):
    LYRIC = "Lyric Poetry"
    NARRATIVE = "Narrative Poetry"
    DRAMATIC = "Dramatic Poetry"
    
# === Analysis Agents ===

lyrical_analyst = Agent(
    name="Lyrical Poetry Analyst",
    instructions="""
        Analyze lyrical poetry with this structure:
            🎭 [Poet]: {poet}
            📜 [Title]: {title}
            ✍️ [Stanza]: 
            {lines}

            🔍 [Analysis]:
            - Theme: {theme}
            - Techniques: {techniques}
            - Era: {era}

            💡 [Interpretation]:
            {detailed_analysis}
        """,
)

narrative_analyst = Agent(
    name="Narrative Poetry Analyst",
    instructions="""
        Analyze narrative poetry with this structure:
            🎭 [Poet]: {poet}
            📜 [Title]: {title}
            ✍️ [Stanza]: 
            {lines}

            🔍 [Analysis]:
            - Plot Summary: {plot}
            - Characters: {characters}
            - Techniques: {techniques}

            📖 [Narrative Devices]:
            {devices}
        """,
)

dramatic_analyst = Agent(
    name="Dramatic Poetry Analyst",
    instructions="""
        Analyze dramatic poetry with this structure:
            🎭 [Poet]: {poet}
            📜 [Title]: {title}
            ✍️ [Stanza]: 
            {lines}

            🎭 [Dramatic Elements]:
            - Speaker: {speaker}
            - Audience: {audience}
            - Conflict: {conflict}

            🎬 [Performance Notes]:
            {performance_notes}
        """,
)

# === Triage Agent ===
triage_agent = Agent(
    name="Poetry_Triage_Agent",
    instructions="""
    Determine poetry type from the clues:
        LYRIC: Personal emotions, musical quality
        NARRATIVE: Storytelling, characters, plot  
        DRAMATIC: Meant for performance, monologue/dialogue

        Respond ONLY with the type(LYRIC/NARRATIVE/DRAMATIC)
    """,
    handoffs=[lyrical_analyst, narrative_analyst, dramatic_analyst],
)

# === Parent Agent ===

parent_agent = Agent(
    name="Poetry_Abalysis_Orchestrator",
    instructions="""
        1. Receive poem input
        2. Route to triage agent
        3. Forward to appropriate analyst
        4. Return formatted analysis
    """,
    handoffs=[triage_agent],
)

# === Display Functions ===
def print_banner():
    banner = """[bold #ffc0cb]
╔════════════════════════════════════════════════════════════════════════════════╗
║ ██████╗  ██████╗ ███████╗████████╗██████╗ ██╗   ██╗                            ║
║ ██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔══██╗╚██╗ ██╔╝                            ║
║ ██████╔╝██║   ██║█████╗     ██║   ██████╔╝ ╚████╔╝                             ║
║ ██╔═══╝ ██║   ██║██╔══╝     ██║   ██╔══██╗  ╚██╔╝                              ║
║ ██║     ╚██████╔╝███████╗   ██║   ██║  ██║   ██║                               ║
║ ╚═╝      ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝                               ║
║                                                                                ║
║            A Multidimensional Poetry Analysis System                           ║
╚════════════════════════════════════════════════════════════════════════════════╝
[/]
    """
    console.print(banner)
    console.print(Panel.fit(
        "[bold #000000] Available Poetry Types: [/]\n"
        "• [bold #000000]Lyric Poetry[/] - Personal emotions & musicality\n"
        "• [bold #000000]Narrative Poetry[/] - Storytelling with characters\n"
        "• [bold #000000]Dramatic Poetry[/] - Performance-focused verse\n\n"
        "Type 'exit' to quit",
        title="📚 Poetry Analysis System",
        border_style="#e21b3c",
        box=DOUBLE,
        style="on #ffc0cb"
    ))

def display_analysis(analysis):
    layout = Layout()
    layout.split_column(
        Layout(name="header"),
        Layout(name="main", ratio=2),
        Layout(name="footer"),
    )
    
    # Header with poet info
    header_content = Text()
    poet_match = re.search(r"\[Poet\]:\s*(.+)", analysis)
    if poet_match:
        header_content.append(poet_match.group(1).strip(), style="bold #e21b3c")
    else:
        header_content.append("Unknown", style="bold red")
    if "[Title]" in analysis:
        header_content.append("\n" + analysis.split("[Title]:")[1].split("\n")[0].strip(), style="italic #e21b3c")  
    
    layout["header"].update(Panel(
        header_content,
        title="🎭 Poet Information",
        border_style="#e08de7"
    ))      
    
    # Main content
    main_content = ""
    if "✍️ [Stanza]:" in analysis:
        main_content += analysis.split("✍️ [Stanza]:")[1].split("🔍 [Analysis]:")[0].strip() + "\n\n"
    if "🔍 [Analysis]:" in analysis:
        main_content += analysis.split("🔍 [Analysis]:")[1].split("💡 [Interpretation]:")[0].strip()
    
    layout["main"].update(Panel(
        Markdown(main_content),
        title="📜 Poem Analysis",
        border_style="#c0fff4"
    ))        
    
    # Footer with additional insights
    
    footer_content = ""
    if "Interpretation" in analysis:
        footer_content += analysis.split("[Interpretation]:")[1].strip()
    elif "Narrative Devices" in analysis:
        footer_content += analysis.split("[Narrative Devices]:")[1].strip()
    elif "Performance Notes" in analysis:
        footer_content += analysis.split("[Performance Notes]:")[1].strip()
        
    layout["footer"].update(Panel(
        Markdown(footer_content),
        title="💡 Deep Insights",
        border_style="#f14c5a"
        
    )) 
    
    console.print(layout)

    
# === Main Application ===
def main():
    
    print_banner()
    
    # Sample poem input
    poem =  """The broken wing of my desire
Shall never soar in skies of fire,
But like a wounded bird shall rest
In the still waters of thy breast.
            """
            
    console.print("\n[bold]Sample Poem:[/bold]")  
    console.print(Panel.fit(poem, border_style="#8feb3a")) 
    
    # Analyze the poem
    console.print("\n[bold]Analyzing the poem...[/bold]")
    
    # Step 1: Determine poetry type
    
    triage_result = Runner.run_sync(triage_agent, poem, run_config=config)
    poetry_type = triage_result.final_output.strip().upper() 
    
    # Step 2: Get appropriate analysis
    if poetry_type == PoetryType.LYRIC.value:
        message = f"""
            🎭 [Poet]: Sarojini Naidu
            📜 [Title]: The Broken Wing
            ✍️ [Stanza]: {poem}

            🔍 [Analysis]:
            - Theme: Unfulfilled love
            - Techniques: Metaphor, Imagery
            - Era: Early 20th century Indian poetry

            💡 [Interpretation]:
            This poem reflects the aching restraint of unfulfilled desires. The metaphor of the broken wing evokes a sense of limitation and loss, while the comforting ‘waters of thy breast’ suggests surrender and solace in love.
    """
        analysis_result = Runner.run_sync(lyrical_analyst, message, run_config=config)
    elif poetry_type == PoetryType.NARRATIVE.value:
        analysis_result = Runner.run_sync(narrative_analyst, poem, run_config=config)
    else:
        analysis_result = Runner.run_sync(dramatic_analyst, poem, run_config=config)
    
    # Display results
    console.print("\n[bold #82d5fc]Analysis Complete![/]")
    console.print(Panel.fit(
        f"Poetry Type: [bold #fc8d45]{poetry_type}[/]",
        border_style="#5bd0bb"
    ))         
    
    display_analysis(analysis_result.final_output)        
            
if __name__ == "__main__":
    main()            
            