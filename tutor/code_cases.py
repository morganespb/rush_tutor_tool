"""'Break This Code': short C snippets with a hidden explanation of what goes wrong."""

from rich.prompt import Prompt
from rich.syntax import Syntax

from tutor.ui import card, show

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
            'The string "Hello" has 5 visible characters plus the null byte.\n'
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
        "run": 'print("Hello")',
        "problem": (
            "sizeof(str) gives the size of the pointer, not the length of the string.\n"
            "On a 64-bit machine, it is usually 8."
        ),
    },
]


def _frame(index: int, show_solution: bool) -> list:
    case = CASES[index]
    frame = [
        card(
            f"[bold yellow]{case['title']}[/bold yellow]\n\n[cyan]Run:[/cyan] {case['run']}",
            title=f"Break This Code {index + 1}/{len(CASES)}",
            style="yellow",
        ),
        Syntax(case["code"].strip(), "c", theme="monokai", line_numbers=True, padding=1),
    ]
    if show_solution:
        frame.append(card(case["problem"], title="What breaks?", style="red"))
    else:
        frame.append(
            card("What happens? Why? How would you fix it?", title="Ask the student first", style="cyan")
        )
    return frame


def code_cases_screen() -> None:
    index, show_solution = 0, False

    while True:
        show(*_frame(index, show_solution))
        choice = Prompt.ask(
            "\n\\[s] show solution  \\[n] next  \\[b] back  \\[q] menu",
            choices=["s", "n", "b", "q"],
            default="n" if show_solution else "s",
        )
        if choice == "q":
            return
        if choice == "s":
            show_solution = True
        else:
            step = 1 if choice == "n" else -1
            index, show_solution = (index + step) % len(CASES), False
