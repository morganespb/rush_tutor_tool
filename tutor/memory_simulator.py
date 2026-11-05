"""Pointer Playground: a step-by-step walk from a variable to a dereferenced pointer."""

from rich.prompt import IntPrompt, Prompt

from tutor.ui import card, show

ADDRESS_A = "0x1000"


def box(content: str, label: str = "") -> str:
    """ASCII box sized to its content, with an optional label on the left."""
    width = max(len(content), 6) + 2
    pad = " " * len(label)
    return (
        f"{pad}+{'-' * width}+\n"
        f"{label}|{content:^{width}}|\n"
        f"{pad}+{'-' * width}+"
    )


def _pointer_to_value(value: int, value_label: str = "      ") -> str:
    """p --> [0x1000] pointing down to [value]."""
    return (
        f"{box(ADDRESS_A, 'p --> ')}\n"
        f"{' ' * 6}     │\n"
        f"{' ' * 6}     ▼\n"
        f"{box(str(value), value_label)}"
    )


def steps(value: int) -> list[tuple[str, str, str]]:
    """(title, style, body) for each step of the lesson."""
    v = str(value)
    return [
        (
            "Variable",
            "cyan",
            f"🏠 [bold]STEP 1 — A variable stores a value[/bold]\n\n"
            f"Code:\n\n    int a = {v};\n\n"
            f"Memory:\n\n      House A\n{box(v, '      ')}\n\n"
            f"Meaning:\n\n    a = {v}",
        ),
        (
            "Address",
            "green",
            f"📍 [bold]STEP 2 — A variable has an address[/bold]\n\n"
            f"Code:\n\n    int a = {v};\n\n"
            f"Memory:\n\n      House A  (address {ADDRESS_A})\n{box(v, '      ')}\n\n"
            f"Meaning:\n\n    a   = {v}\n    &a  = {ADDRESS_A}  (address of a)",
        ),
        (
            "Pointer",
            "magenta",
            f"📮 [bold]STEP 3 — A pointer stores an address[/bold]\n\n"
            f"Code:\n\n    int a = {v};\n    int *p = &a;\n\n"
            f"Memory:\n\n{_pointer_to_value(value)}\n\n"
            f"Meaning:\n\n    p = {ADDRESS_A}\n\n"
            f"p does NOT store {v}. p stores the address of a.",
        ),
        (
            "Dereference",
            "yellow",
            f"⭐ [bold]STEP 4 — Dereferencing with *[/bold]\n\n"
            f"Code:\n\n    *p\n\n"
            f"Meaning: go to the address stored inside p.\n\n"
            f"{_pointer_to_value(value, 'a --> ')}\n\n"
            f"Result:\n\n    *p = {v}",
        ),
        (
            "Why pointers?",
            "bright_blue",
            f"🎯 [bold]STEP 5 — Why pointers matter in C[/bold]\n\n"
            f"Without pointer:   function(a)\n"
            f"    The function receives a COPY of {v}. The original is not changed.\n\n"
            f"With pointer:      function(&a)\n"
            f"    The function receives the ADDRESS of a and can modify the real variable.\n\n"
            f"Why C needs pointers:\n\n"
            f"    ✓ modify variables inside functions\n"
            f"    ✓ avoid copying large data\n"
            f"    ✓ work with arrays and strings\n"
            f"    ✓ allocate memory with malloc\n"
            f"    ✓ build linked lists and trees",
        ),
    ]


def memory_simulator_screen() -> None:
    show(card("Pick a value and follow it through memory, one step at a time.", title="Pointer Playground"))
    value = IntPrompt.ask("Choose a value for variable a", default=42)

    lesson = steps(value)
    index = 0
    while True:
        title, style, body = lesson[index]
        show(card(body, title=f"{title} ({index + 1}/{len(lesson)})", style=style))

        last = index == len(lesson) - 1
        choice = Prompt.ask(
            "\n\\[n] next  \\[b] back  \\[q] menu",
            choices=["n", "b", "q"],
            default="q" if last else "n",
        )
        if choice == "q" or (choice == "n" and last):
            return
        index = max(index - 1, 0) if choice == "b" else index + 1
