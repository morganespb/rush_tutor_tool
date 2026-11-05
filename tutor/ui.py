"""Shared console and rendering helpers used by every screen."""

from textwrap import dedent

from rich.console import Console, RenderableType
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()


def card(text: str, title: str = "", style: str = "cyan") -> Panel:
    """A panel whose text is dedented, so lessons can be written indented in code."""
    return Panel(
        dedent(text).strip("\n"),
        title=f"[bold]{title}[/bold]" if title else None,
        border_style=style,
        padding=(1, 2),
    )


def show(*renderables: RenderableType) -> None:
    """Clear the screen and draw a full frame in a single write (no flicker)."""
    with console:  # buffers output until the block ends
        console.clear()
        for renderable in renderables:
            console.print(renderable)


def wait() -> None:
    Prompt.ask("\n[bold green]Press ENTER to continue[/bold green]", default="", show_default=False)
