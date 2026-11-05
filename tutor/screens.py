"""Simple lesson screens: draw one frame, then wait for ENTER."""

from rich.panel import Panel

from tutor import diagrams
from tutor.ui import card, console, show, wait


def _lesson(*renderables) -> None:
    show(*renderables)
    wait()


def argc_argv_screen() -> None:
    _lesson(
        card(
            """
            [bold cyan]argc[/bold cyan] = number of arguments passed to the program.
            [bold cyan]argv[/bold cyan] = array of strings (char **).
            """,
            title="argc / argv",
            style="green",
        ),
        diagrams.argv_table(["./rush", "hello", "world"], title="Command: ./rush hello world"),
        diagrams.argv_arrows_panel(),
    )


def memory_screen() -> None:
    _lesson(diagrams.memory_panel())


def fd_screen() -> None:
    _lesson(diagrams.fd_panel())


def write_screen() -> None:
    _lesson(diagrams.write_panel())


def redirections_screen() -> None:
    _lesson(diagrams.redirections_panel())


def common_mistakes_screen() -> None:
    _lesson(diagrams.common_mistakes_panel())


def goodbye_screen() -> None:
    """Printed after leaving the full-screen view, so it stays in the terminal."""
    console.print(
        Panel.fit(
            "[bold yellow]🚀 42 RUSH00 TUTOR TOOL 🚀[/bold yellow]\n\n"
            "Keep teaching. Keep learning. Keep breaking code. 😉\n"
            "Good luck with your evaluations!\n\n"
            "[dim]Made with ❤️  for 42 tutors and students.[/dim]",
            title="Goodbye",
            border_style="bright_green",
            padding=(1, 4),
        )
    )
