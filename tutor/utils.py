import os
import select
import sys

from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.prompt import Prompt
from rich.theme import Theme

try:
    import termios
    import tty
except ImportError:  # Windows: fall back to ENTER-based input
    termios = None


class TutorHighlighter(RegexHighlighter):
    """Colors the C / memory vocabulary automatically in every panel."""

    base_style = "tutor."
    highlights = [
        r"(?P<number>(?<![\w.])\d+(?![\w.]))",
        r"(?P<string>\"[^\"\n]*\")",
        r"(?P<type>\b(?:char|int|void|return)\b\s*\**)",
        r"(?P<func>\b(?:write|read|printf|sizeof|malloc|free|main)\b)(?=\()",
        r"(?P<argv>\bargv\[\w+\]|\bargc\b|\bargv\b)",
        r"(?P<pointer>(?<![\w*])[&*]{1,2}[a-z]\b)",
        r"(?P<address>\b0x[0-9a-fA-F]+\b)",
        r"(?P<null>\bNULL\b|'\\0')",
        r"(?P<fd>\b(?:stdin|stdout|stderr)\b|\bfd \d\b)",
        r"(?P<arrow>[─-]*[►>→▼]|\|\s*$|-->)",
        r"(?P<good>✓)",
        r"(?P<bad>❌)",
    ]


THEME = Theme(
    {
        "tutor.number": "bold bright_magenta",
        "tutor.string": "green",
        "tutor.type": "bold blue",
        "tutor.func": "bold yellow",
        "tutor.argv": "bold cyan",
        "tutor.pointer": "bold bright_yellow",
        "tutor.address": "bold magenta",
        "tutor.null": "bold red",
        "tutor.fd": "bold bright_blue",
        "tutor.arrow": "bright_cyan",
        "tutor.good": "bold green",
        "tutor.bad": "bold red",
    }
)

# One console for the whole app, so the colors apply everywhere.
console = Console(highlighter=TutorHighlighter(), theme=THEME)

# Last key pressed, read by app.py to flip between lessons.
last_key = None

NAV_HINT = (
    "[bold cyan]←[/bold cyan] previous lesson   "
    "[bold cyan]→[/bold cyan] next lesson   "
    "[bold cyan]any key[/bold cyan] menu"
)


def clear():
    console.clear()


def getkey() -> str:
    """Read one key press without ENTER. Returns 'left', 'right', 'up', 'down',
    'enter', 'space', 'esc' or the character itself."""
    global last_key

    if termios is None or not sys.stdin.isatty():
        line = sys.stdin.readline()
        if line == "":
            raise EOFError
        key = line.strip().lower() or "enter"
    else:
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            data = os.read(fd, 1)
            if data == b"\x1b":
                while select.select([fd], [], [], 0.03)[0]:
                    data += os.read(fd, 1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

        arrows = {b"[A": "up", b"[B": "down", b"[C": "right", b"[D": "left"}
        if data.startswith(b"\x1b"):
            key = arrows.get(data[1:3].replace(b"O", b"["), "esc")
        elif data in (b"\r", b"\n"):
            key = "enter"
        elif data == b" ":
            key = "space"
        else:
            key = data.decode(errors="ignore").lower()

    last_key = key
    return key


def wait(hint: str = NAV_HINT) -> str:
    console.print(f"\n[dim]{hint}[/dim]", justify="center", highlight=False)
    return getkey()


def separator():
    console.rule(style="cyan")


def ask(*args, **kwargs):
    """Prompt.ask using the shared console."""
    return Prompt.ask(*args, console=console, **kwargs)
