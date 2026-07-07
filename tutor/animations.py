from time import sleep
from rich.console import Console

console = Console()


def reveal(text: str, delay: float = 0.04) -> None:
    """
    Print text line by line.
    """

    for line in text.splitlines():
        console.print(line)
        sleep(delay)


def divider() -> None:
    console.rule(style="cyan")


def title(text: str) -> None:
    console.rule(f"[bold yellow]{text}[/bold yellow]")
