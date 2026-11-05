from rich.panel import Panel
from rich.text import Text
from tutor.utils import wait, getkey
from tutor.diagrams import argv_table, fd_panel, memory_panel, write_panel, redirections_panel, common_mistakes_panel
from tutor.animations import reveal, show
from rich.prompt import Prompt

from tutor.utils import console


#def pause():
#    """Wait for the user before returning."""
#   Prompt.ask("\n[green]Press ENTER to continue[/green]", default="")


#def home_screen() -> None:
#"""Display the welcome screen."""
#
#    console.clear()
#
#    console.print(
#        Panel(
#            "[bold yellow]🚀 Welcome to the 42 Tutor Toolkit[/bold yellow]\n\n"
#            "This application helps explain:\n\n"
#            "1. argc / argv\n"
#            "2. Memory visualization\n"
#            "3. File descriptors\n"
#            "4. write()\n"
#            "5. Shell redirections\n"
#            "6. Common mistakes\n"
#            "7. Interactive simulator\n"
#            "8. Break this code\n"
#            "9. Memory Simulator\n"
#            "10. Argv Playground\n"
#            "[dim]Choose a lesson from the menu.[/dim]",
#            title="Home",
#            border_style="yellow",
#        )
#    )

MENU = [
    ("1", "📦 argc / argv"),
    ("2", "🏠 Memory & Pointers"),
    ("3", "📮 File Descriptors"),
    ("4", "✍️  write()"),
    ("5", "🔀 Shell Redirections"),
    ("6", "⚠️  Common Mistakes"),
    ("7", "⚡ Live argc/argv Simulator"),
    ("8", "💥 Break This Code"),
    ("9", "🧠 Pointer Playground"),
    ("10", "🧬 char **argv Playground"),
]
selected = 0


def home_screen() -> str:
    """Menu: ↑ ↓ + ENTER, or press the lesson number directly (0 = 10)."""
    global selected
    animate = True

    while True:
        lines = []
        for i, (key, label) in enumerate(MENU):
            if i == selected:
                lines.append(f"[black on bright_cyan] ▶ {key:<3} {label}  [/black on bright_cyan]")
            else:
                lines.append(f"   [bold cyan]{key:<3}[/bold cyan] {label}")

        show(
            Panel(
                Text.from_markup(
                    "\n[bold bright_cyan]🚀 42 RUSH00 TUTOR TOOL[/bold bright_cyan]\n\n"
                    "Interactive visual explanations for C basics.\n\n"
                    + "\n".join(lines)
                    + "\n\n   [bold red]q[/bold red]   Quit\n"
                ),
                title="42 Tutor Mode",
                border_style="bright_cyan",
                padding=(1, 4),
            ),
            "[dim][bold cyan]↑ ↓[/bold cyan] move   [bold cyan]enter[/bold cyan] open   "
            "[bold cyan]1-9, 0[/bold cyan] jump   [bold cyan]q[/bold cyan] quit[/dim]",
            animate=animate,
        )
        animate = False

        key = getkey()
        if key == "up":
            selected = (selected - 1) % len(MENU)
        elif key == "down":
            selected = (selected + 1) % len(MENU)
        elif key in ("enter", "space", "right"):
            return MENU[selected][0]
        elif key in ("q", "esc"):
            return "q"
        elif key == "0":
            selected = 9
            return "10"
        elif key in [k for k, _ in MENU]:
            selected = int(key) - 1
            return key

def argc_argv_screen() -> None:
    show(
        Panel(
            "[bold cyan]argc[/bold cyan] = Number of arguments passed to the program.\n"
            "[bold cyan]argv[/bold cyan] = Array of strings (char **).",
            title="argc / argv",
            border_style="green",
        ),
        argv_table("./rush hello world"),
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

    ✓ argv\\[argc] is ALWAYS NULL.
    """,
            title="Memory visualization",
            border_style="yellow",
        ),
    )

    wait()
def fd_screen() -> None:
    show(fd_panel())
    wait()

def write_screen() -> None:
    show(write_panel())
    wait()

def redirections_screen() -> None:
    show(redirections_panel())
    wait()

def common_mistakes_screen() -> None:
    show(common_mistakes_panel())
    wait()

def memory_screen() -> None:
    show(memory_panel())
    wait()

def goodbye_screen() -> None:
    show(
        Panel(
            """
    [bold bright_cyan]
            Thank you for using
    [/bold bright_cyan]

    [bold yellow]
          🚀 42 RUSH00 TUTOR TOOL 🚀
    [/bold yellow]

    ──────────────────────────────────────────────

    Keep teaching.
    Keep learning.
    Keep breaking code. 😉

    Good luck with your evaluations!

    ──────────────────────────────────────────────

    [dim]
    Made with ❤️ for 42 tutors and students.
    [/dim]
    """,
            title="Goodbye",
            border_style="bright_green",
            padding=(1, 4),
        )
    )

    wait("press any key to exit")
