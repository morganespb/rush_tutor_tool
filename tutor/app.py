"""Main menu. Add a lesson by adding one line to MENU."""

from rich.prompt import Prompt

from tutor.argv_tools import argv_playground_screen, simulator_screen
from tutor.code_cases import code_cases_screen
from tutor.memory_simulator import memory_simulator_screen
from tutor.screens import (
    argc_argv_screen,
    common_mistakes_screen,
    fd_screen,
    goodbye_screen,
    memory_screen,
    redirections_screen,
    write_screen,
)
from tutor.ui import card, console, show

MENU = [
    ("1", "📦 argc / argv", argc_argv_screen),
    ("2", "🏠 Memory & Pointers", memory_screen),
    ("3", "📮 File Descriptors", fd_screen),
    ("4", "✍️  write()", write_screen),
    ("5", "🔀 Shell Redirections", redirections_screen),
    ("6", "⚠️  Common Mistakes", common_mistakes_screen),
    ("7", "⚡ Live argc/argv Simulator", simulator_screen),
    ("8", "💥 Break This Code", code_cases_screen),
    ("9", "🧠 Pointer Playground", memory_simulator_screen),
    ("10", "🧬 char **argv Playground", argv_playground_screen),
]
SCREENS = {key: screen for key, _, screen in MENU}


def home_screen() -> str:
    entries = "\n".join(f"[bold cyan]{key:<3}[/bold cyan] {label}" for key, label, _ in MENU)
    show(
        card(
            "[bold bright_cyan]🚀 42 RUSH00 TUTOR TOOL[/bold bright_cyan]\n\n"
            "Interactive visual explanations for C basics.\n\n"
            f"{entries}\n\n"
            "[bold red]q[/bold red]   Quit",
            title="42 Tutor Mode",
            style="bright_cyan",
        )
    )
    return Prompt.ask(
        "\n[bold green]Choose a lesson[/bold green]",
        choices=[*SCREENS, "q"],
        show_choices=False,
    )


def run() -> None:
    try:
        # Alternate screen: the app gets a clean full-screen canvas and the
        # user's terminal history is restored untouched on exit.
        with console.screen():
            while (choice := home_screen()) != "q":
                SCREENS[choice]()
    except (KeyboardInterrupt, EOFError):
        pass
    goodbye_screen()
