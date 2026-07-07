from rich.console import Console
from rich.panel import Panel
from tutor.utils import wait
from tutor.diagrams import argv_table, fd_panel, memory_panel, write_panel, redirections_panel, common_mistakes_panel
from tutor.animations import reveal

console = Console()


#def pause():
#    """Wait for the user before returning."""
#   Prompt.ask("\n[green]Press ENTER to continue[/green]", default="")


def home_screen() -> None:
    """Display the welcome screen."""

    console.clear()

    console.print(
        Panel(
            "[bold yellow]🚀 Welcome to the 42 Tutor Toolkit[/bold yellow]\n\n"
            "This application helps explain:\n\n"
            "1. argc / argv\n"
            "2. Memory visualization\n"
            "3. File descriptors\n"
            "4. write()\n"
            "5. Shell redirections\n"
            "6. Common mistakes\n"
            "7. Interactive simulator\n\n"
            "[dim]Choose a lesson from the menu.[/dim]",
            title="Home",
            border_style="yellow",
        )
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
