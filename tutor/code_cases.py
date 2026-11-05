from rich.panel import Panel
from rich.syntax import Syntax
from tutor.utils import getkey
from tutor.animations import show

from tutor.utils import console

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
    animate = True

    while True:
        case = CASES[index]
        frame = [
            Panel(
                f"[bold yellow]{case['title']}[/bold yellow]\n\n"
                f"[cyan]Run:[/cyan] {case['run']}",
                title=f"Break This Code {index + 1}/{len(CASES)}",
                border_style="yellow",
            ),
            Syntax(case["code"].strip(), "c", theme="monokai", line_numbers=True, padding=1),
        ]

        if show_solution:
            frame.append(
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

        frame.append(
            "\n[dim][bold cyan]space[/bold cyan] show solution   "
            "[bold cyan]←  →[/bold cyan] previous / next case   "
            "[bold cyan]q[/bold cyan] menu[/dim]"
        )
        show(*frame, animate=animate)
        animate = False

        choice = getkey()

        if choice in ("s", "space", "enter", "down"):
            show_solution = True
        elif choice in ("n", "right"):
            index = (index + 1) % len(CASES)
            show_solution = False
            animate = True
        elif choice in ("b", "left"):
            index = (index - 1) % len(CASES)
            show_solution = False
            animate = True
        elif choice in ("q", "esc"):
            break
