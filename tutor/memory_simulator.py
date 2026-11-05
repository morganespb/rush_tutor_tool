from rich.panel import Panel
from rich.prompt import IntPrompt
from tutor.utils import wait
from tutor.animations import show

from tutor import utils
from tutor.utils import console

ADDRESS_A = "0x1000"
STEP_HINT = (
    "[bold cyan]←[/bold cyan] previous step   "
    "[bold cyan]→ / space[/bold cyan] next step   "
    "[bold cyan]q[/bold cyan] menu"
)


def step1(value: int) -> None:
    show(
        Panel(
            f"""
🏠 STEP 1 — A variable stores a value

Code:

    int a = {value};

Memory:

        House A

      +--------+
      | {value:^6} |
      +--------+

Meaning:

    a = {value}
""",
            title="Variable",
            border_style="cyan",
        )
    )
    wait(STEP_HINT)


def step2(value: int) -> None:
    show(
        Panel(
            f"""
📍 STEP 2 — A variable has an address

Code:

    int a = {value};

Memory:

        House A

      +--------+
      | {value:^6} |
      +--------+

Address:

    &a = {ADDRESS_A}

Meaning:

    a   = {value}
    &a  = address of a
""",
            title="Address",
            border_style="green",
        )
    )
    wait(STEP_HINT)


def step3(value: int) -> None:
    show(
        Panel(
            f"""
📮 STEP 3 — A pointer stores an address

Code:

    int a = {value};
    int *p = &a;

Memory:

        p stores {ADDRESS_A}

      +----------+
p --> | {ADDRESS_A} |
      +----------+
           |
           v
        House A
      +--------+
      | {value:^6} |
      +--------+

Meaning:

    p = {ADDRESS_A}

p does NOT store {value}.
p stores the address of a.
""",
            title="Pointer",
            border_style="magenta",
        )
    )
    wait(STEP_HINT)


def step4(value: int) -> None:
    show(
        Panel(
            f"""
⭐ STEP 4 — Dereferencing with *

Code:

    *p

Meaning:

    Go to the address stored inside p.

      +----------+
p --> | {ADDRESS_A} |
      +----------+
           |
           v
      +--------+
a --> | {value:^6} |
      +--------+

Result:

    *p = {value}
""",
            title="Dereference",
            border_style="yellow",
        )
    )
    wait(STEP_HINT)


def step5(value: int) -> None:
    show(
        Panel(
            f"""
🎯 STEP 5 — Why pointers matter in C

Without pointer:

    function(a)

    The function receives a COPY of {value}.
    The original variable is not changed.

With pointer:

    function(&a)

    The function receives the ADDRESS of a.
    It can go to the real variable and modify it.


Example idea:

    a = {value}

    change_copy(a)
        -> modifies only a copy

    change_real(&a)
        -> can modify the original a


Why C needs pointers:

    ✓ modify variables inside functions
    ✓ avoid copying large data
    ✓ work with arrays and strings
    ✓ allocate memory with malloc
    ✓ build linked lists and trees
""",
            title="Why pointers?",
            border_style="bright_blue",
        )
    )
    wait(STEP_HINT)


def memory_simulator_screen() -> None:
    console.clear()

    value = IntPrompt.ask(
        "Choose a value for variable a",
        default=42,
    )

    steps = [step1, step2, step3, step4, step5]
    i = 0
    while i < len(steps):
        steps[i](value)
        key = utils.last_key
        if key in ("q", "esc"):
            break
        i = max(i - 1, 0) if key == "left" else i + 1
