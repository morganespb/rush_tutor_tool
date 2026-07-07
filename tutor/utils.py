from rich.console import Console
from rich.prompt import Prompt

console = Console()


def clear():
    console.clear()


def wait():
    Prompt.ask(
        "\n[bold green]Press ENTER to continue[/bold green]",
        default=""
    )


def separator():
    console.rule(style="cyan")
