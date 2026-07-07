from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from tutor.utils import wait

console = Console()

CASES = [
    {
        "title": "Accessing argv[1] without checking argc",
        "code": """
#include <stdio.h>

int main(int argc, char **argv)
{
    printf("%s\\n", argv[1]);
    return (0);
}
""",
        "run": "./rush",
        "problem": (
            "argc == 1, so argv[1] is NULL.\n"
            "The program may segfault because it uses argv[1] without checking argc."
        ),
    },
    {
        "title": "Wrong write count",
        "code": """
#include <unistd.h>

int main(void)
{
    write(1, "Hello", 10);
    return (0);
}
""",
        "run": "./rush",
        "problem": (
            "The string \"Hello\" has 5 visible characters plus the null byte.\n"
            "write() does not stop at '\\0'. It writes exactly 10 bytes.\n"
            "So it may print garbage after Hello."
        ),
    },
    {
        "title": "Using sizeof on a pointer",
        "code": """
#include <unistd.h>

void print(char *str)
{
    write(1, str, sizeof(str));
}
""",
        "run": "print(\"Hello\")",
        "problem": (
            "sizeof(str) gives the size of the pointer, not the length of the string.\n"
            "On a 64-bit machine, it is usually 8."
        ),
    },
]


def code_cases_screen() -> None:
    index = 0

    while True:
        case = CASES[index]
        console.clear()

        console.print(
            Panel(
                f"[bold yellow]{case['title']}[/bold yellow]\n\n"
                f"[cyan]Run:[/cyan] {case['run']}",
                title=f"Break This Code {index + 1}/{len(CASES)}",
                border_style="yellow",
            )
        )

        syntax = Syntax(case["code"].strip(), "c", theme="monokai", line_numbers=True)
        console.print(syntax)

        console.print(
            Panel(
                case["problem"],
                title="What breaks?",
                border_style="red",
            )
        )

        choice = Prompt.ask(
            "\n[n] next  [b] back  [q] menu",
            choices=["n", "b", "q"],
            default="n",
        )

        if choice == "n":
            index = (index + 1) % len(CASES)
        elif choice == "b":
            index = (index - 1) % len(CASES)
        elif choice == "q":
            break

    wait()
