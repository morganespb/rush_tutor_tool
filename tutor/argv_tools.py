"""Interactive argc / argv screens. Commands are parsed like a real shell (shlex)."""

import shlex

from rich.markup import escape
from rich.prompt import Prompt

from tutor.diagrams import argv_table
from tutor.ui import card, console, show, wait

SIMULATOR_HELP = card(
    """
    [bold cyan]Type a fake command and I will build argc / argv.[/bold cyan]

    Try:
      ./rush hello world
      ./rush "hello world"
      ./rush ""
      ./rush

    [dim]Type q to return to the menu.[/dim]
    """,
    title="Live argc / argv Simulator",
)


def parse(command: str) -> list[str] | None:
    """Split like a shell; print the error and return None if quoting is broken."""
    try:
        return shlex.split(command)
    except ValueError as error:
        console.print(f"[bold red]Shell parsing error:[/bold red] {error}")
        return None


def simulator_screen() -> None:
    show(SIMULATOR_HELP)
    while True:
        command = Prompt.ask("\n[bold]Command[/bold]")
        if command.strip() == "q":
            return

        argv = parse(command)
        if argv is None:
            continue
        if not argv:
            console.print("[bold red]Empty command.[/bold red] A real program always has argv[0].")
            continue

        # Redraw the help + the new result in one frame instead of scrolling.
        show(SIMULATOR_HELP, argv_table(argv, title=f"$ {escape(command)}"))


def argv_playground_screen() -> None:
    show(
        card(
            "Type a command and see how [bold]char **argv[/bold] looks in memory.",
            title="char **argv Playground",
            style="bright_cyan",
        )
    )
    command = Prompt.ask("Command", default="./rush hello world")
    argv = parse(command)
    if not argv:
        wait()
        return

    argc = len(argv)
    boxes = "\n".join(
        f"argv[{i}]  [cyan]+----------+[/cyan]\n"
        f"         [cyan]| address  |[/cyan] ──────► [yellow]\"{escape(arg)}\"[/yellow]\n"
        f"         [cyan]+----------+[/cyan]"
        for i, arg in enumerate(argv)
    )

    show(
        card(
            f"Command:  [bold]{escape(command)}[/bold]\n"
            f"argc = {argc}\n\n"
            "argv is a list of addresses. Each address points to a string.\n\n"
            f"{boxes}\n"
            f"argv[{argc}]  [red]+----------+[/red]\n"
            f"         [red]|   NULL   |[/red]\n"
            f"         [red]+----------+[/red]\n\n"
            "[bold]Why char ** ?[/bold]\n\n"
            "    char *    = one string       (argv[0], argv[1], ...)\n"
            "    char **   = list of strings  (argv itself)",
            title="char **argv Playground",
            style="bright_cyan",
        )
    )
    wait()
