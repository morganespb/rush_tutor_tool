import shlex

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from tutor.utils import wait

console = Console()


def argv_playground_screen() -> None:
    console.clear()

    command = Prompt.ask(
        "Type a command",
        default="./rush hello world",
    )

    try:
        argv = shlex.split(command)
    except ValueError as error:
        console.print(f"[bold red]Parsing error:[/bold red] {error}")
        wait()
        return

    argc = len(argv)

    drawing = f"""
Command:

    {command}

argc = {argc}


char **argv means:

    argv
     |
     v

argv is a list of addresses.

Each address points to a string.


Visual memory:

"""

    for i, arg in enumerate(argv):
        drawing += f"""
    argv[{i}]
    +----------+
    | address  | -----------> "{arg}"
    +----------+
"""

    drawing += f"""
    argv[{argc}]
    +----------+
    |  NULL    |
    +----------+


Why char ** ?

    char *    = one string

    char **   = list of strings


Example:

    argv[0] is a char *
    argv[1] is a char *

    argv itself is a char **
"""

    console.print(
        Panel(
            drawing,
            title="char **argv Playground",
            border_style="bright_cyan",
        )
    )

    wait()
