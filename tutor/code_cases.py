from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from tutor.utils import wait

console = Console()

CASES = [
    {
        "title": "Printing arguments",
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
        "title": "Are you using write() properly?",
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
        "title": "Are you sure about the count?",
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
    show_solution = False

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

        if show_solution:
            console.print(
                Panel(
                    case["problem"],
                    title="What breaks?",
                    border_style="red",
                )
            )
        #else:
        #    console.print(
        #        Panel(
        #            "[bold cyan]Ask the student first:[/bold cyan]\n\n"
        #            "What happens?\n"
        #            "Why?\n"
        #            "How would you fix it?",
        #            title="Think first",
        #            border_style="cyan",
        #        )
        #    )

        choice = Prompt.ask(
            "\n[s] show solution  [n] next  [b] back  [q] menu",
            choices=["s", "n", "b", "q"],
            default="s",
        )

        if choice == "s":
            show_solution = True
        elif choice == "n":
            index = (index + 1) % len(CASES)
            show_solution = False
        elif choice == "b":
            index = (index - 1) % len(CASES)
            show_solution = False
        elif choice == "q":
            break

    wait()
