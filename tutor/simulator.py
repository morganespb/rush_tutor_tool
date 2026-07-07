import shlex
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from tutor.diagrams import argv_table
from tutor.utils import wait

console = Console()


def simulator_screen() -> None:
    console.clear()

    console.print(
        Panel(
            "[bold cyan]Type a fake command and I will build argc / argv.[/bold cyan]\n\n"
            "Try:\n"
            "  ./rush hello world\n"
            "  ./rush \"hello world\"\n"
            "  ./rush \"\"\n"
            "  ./rush\n\n"
            "[dim]Type q to return to the menu.[/dim]",
            title="Live argc / argv Simulator",
            border_style="cyan",
        )
    )

    while True:
        command = Prompt.ask("\nCommand")

        if command == "q":
            break

        try:
            console.print(argv_table_from_shell(command))
        except ValueError as error:
            console.print(f"[bold red]Shell parsing error:[/bold red] {error}")
    wait()


def argv_table_from_shell(command: str):
    argv = shlex.split(command)
    argc = len(argv)

    if argc == 0:
        return Panel(
            "[bold red]Empty command.[/bold red]\n\n"
            "A real executed program usually has at least argv[0].",
            border_style="red",
        )

    # reuse same visual logic but with correct shell parsing.
    fake_command = "\n".join(argv)
    return argv_table_from_list(argv)


def argv_table_from_list(argv: list[str]):
    from rich.table import Table

    argc = len(argv)

    table = Table(
        title=f"argc = {argc}",
        border_style="cyan",
        show_lines=True,
    )

    table.add_column("Index", style="bold cyan", justify="center")
    table.add_column("Value", style="yellow")

    for i, arg in enumerate(argv):
        table.add_row(f"argv[{i}]", f'"{arg}"')

    table.add_row(f"argv[{argc}]", "[bold red]NULL[/bold red]")

    return table
