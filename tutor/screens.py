from rich.console import Console
from rich.panel import Panel
from tutor.utils import wait
from tutor.diagrams import argv_table, fd_panel, memory_panel, write_panel, redirections_panel, common_mistakes_panel
from tutor.animations import reveal
from rich.prompt import Prompt

console = Console()


#def pause():
#    """Wait for the user before returning."""
#   Prompt.ask("\n[green]Press ENTER to continue[/green]", default="")


#def home_screen() -> None:
#"""Display the welcome screen."""
#
#    console.clear()
#
#    console.print(
#        Panel(
#            "[bold yellow]🚀 Welcome to the 42 Tutor Toolkit[/bold yellow]\n\n"
#            "This application helps explain:\n\n"
#            "1. argc / argv\n"
#            "2. Memory visualization\n"
#            "3. File descriptors\n"
#            "4. write()\n"
#            "5. Shell redirections\n"
#            "6. Common mistakes\n"
#            "7. Interactive simulator\n"
#            "8. Break this code\n"
#            "9. Memory Simulator\n"
#            "10. Argv Playground\n"
#            "[dim]Choose a lesson from the menu.[/dim]",
#            title="Home",
#            border_style="yellow",
#        )
#    )

def home_screen() -> str:
    console.clear()

    console.print(
        Panel(
            """
    [bold bright_cyan]🚀 42 RUSH00 TUTOR TOOL[/bold bright_cyan]

    Interactive visual explanations for C basics.

    [bold cyan]1[/bold cyan]   📦 argc / argv
    [bold cyan]2[/bold cyan]   🏠 Memory & Pointers
    [bold cyan]3[/bold cyan]   📮 File Descriptors
    [bold cyan]4[/bold cyan]   ✍️  write()
    [bold cyan]5[/bold cyan]   🔀 Shell Redirections
    [bold cyan]6[/bold cyan]   ⚠️  Common Mistakes
    [bold cyan]7[/bold cyan]   ⚡ Live argc/argv Simulator
    [bold cyan]8[/bold cyan]   💥 Break This Code
    [bold cyan]9[/bold cyan]   🧠 Pointer Playground
    [bold cyan]10[/bold cyan]  🧬 char **argv Playground

    [bold red]q[/bold red]   Quit
    """,
            title="42 Tutor Mode",
            border_style="bright_cyan",
            padding=(1, 4),
        )
    )

    return Prompt.ask(
        "\n[bold green]Choose a lesson[/bold green]",
        choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "q"],
    )

def argc_argv_screen() -> None:
    console.clear()

    console.print(
        Panel(
            "[bold cyan]argc[/bold cyan] = Number of arguments passed to the program.\n"
            "[bold cyan]argv[/bold cyan] = Array of strings (char **).",
            title="argc / argv",
            border_style="green",
        )
    )

    console.print(argv_table("./rush hello world"))

    console.print(
        Panel(
            """
    Visual representation

    argv
     │
     ▼

    argv[0] ─────► "./rush"

    argv[1] ─────► "hello"

    argv[2] ─────► "world"

    argv[3] ─────► NULL


    Remember:

    ✓ argc counts ALL arguments.

    ✓ argv[0] is ALWAYS the program name.

    ✓ argv[1] is the first user argument.

    ✓ argv[argc] is ALWAYS NULL.
    """,
                title="Memory visualization",
                border_style="yellow",
            )
        )

    wait()
def fd_screen() -> None:
    console.clear()
    console.print(fd_panel())
    wait()

def write_screen() -> None:
    console.clear()
    console.print(write_panel())
    wait()

def redirections_screen() -> None:
    console.clear()
    console.print(redirections_panel())
    wait()

def common_mistakes_screen() -> None:
    console.clear()
    console.print(common_mistakes_panel())
    wait()

def memory_screen() -> None:
    console.clear()
    console.print(memory_panel())
    wait()

def goodbye_screen() -> None:
    console.clear()

    console.print(
        Panel(
            """
    [bold bright_cyan]
            Thank you for using
    [/bold bright_cyan]

    [bold yellow]
          🚀 42 RUSH00 TUTOR TOOL 🚀
    [/bold yellow]

    ──────────────────────────────────────────────

    Keep teaching.
    Keep learning.
    Keep breaking code. 😉

    Good luck with your evaluations!

    ──────────────────────────────────────────────

    [dim]
    Made with ❤️ for 42 tutors and students.
    [/dim]
    """,
            title="Goodbye",
            border_style="bright_green",
            padding=(1, 4),
        )
    )

    wait()
