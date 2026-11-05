from time import sleep

from rich.panel import Panel

from tutor.utils import console


def reveal(text: str, delay: float = 0.04) -> None:
    """
    Print text line by line.
    """

    for line in text.splitlines():
        console.print(line)
        sleep(delay)


def show(*renderables, animate: bool = True, delay: float = 0.008) -> None:
    """
    Clear the screen and draw a full screen at once (no flicker),
    sliding it in line by line for a smooth effect.
    """

    with console.capture() as capture:
        for renderable in renderables:
            # Color the C vocabulary inside panels too (see TutorHighlighter).
            if isinstance(renderable, Panel) and isinstance(renderable.renderable, str):
                renderable.renderable = console.render_str(renderable.renderable, highlight=True)
            console.print(renderable)
    lines = capture.get().splitlines(keepends=True)

    console.clear()
    if not animate or not console.is_terminal:
        console.file.write("".join(lines))
    else:
        for line in lines:
            console.file.write(line)
            console.file.flush()
            sleep(delay)
    console.file.flush()


def divider() -> None:
    console.rule(style="cyan")


def title(text: str) -> None:
    console.rule(f"[bold yellow]{text}[/bold yellow]")
