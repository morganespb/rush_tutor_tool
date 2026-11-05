"""Static lesson content: reusable tables and panels."""

from rich.markup import escape
from rich.panel import Panel
from rich.table import Table

from tutor.ui import card


def argv_table(argv: list[str], title: str = "") -> Table:
    """Table showing each argv entry, ending with the NULL terminator."""
    argc = len(argv)
    table = Table(
        title=title or f"argc = {argc}",
        border_style="cyan",
        show_lines=True,
    )
    table.add_column("Index", justify="center", style="bold cyan")
    table.add_column("Value", style="yellow")
    table.add_column("Type", justify="center", style="green")

    for i, arg in enumerate(argv):
        table.add_row(f"argv[{i}]", f'"{escape(arg)}"', "char *")
    table.add_row(f"argv[{argc}]", "[bold red]NULL[/bold red]", "end marker")
    return table


def argv_arrows_panel() -> Panel:
    return card(
        """
        argv
         │
         ▼
        argv[0] ─────► "./rush"
        argv[1] ─────► "hello"
        argv[2] ─────► "world"
        argv[3] ─────► NULL

        [bold]Remember:[/bold]

        ✓ argc counts ALL arguments.
        ✓ argv[0] is ALWAYS the program name.
        ✓ argv[1] is the first user argument.
        ✓ argv\\[argc] is ALWAYS NULL.
        """,
        title="Memory visualization",
        style="yellow",
    )


def fd_panel() -> Panel:
    return card(
        """
        FILE DESCRIPTORS = numbers used by the OS to access streams

        When a program starts, it already has 3 open doors:

        ┌───────────┬──────────┬────────────────────────────┐
        │ FD number │ Name     │ Usually connected to       │
        ├───────────┼──────────┼────────────────────────────┤
        │ 0         │ stdin    │ keyboard / input           │
        │ 1         │ stdout   │ terminal / normal output   │
        │ 2         │ stderr   │ terminal / error output    │
        └───────────┴──────────┴────────────────────────────┘

        Visual:

                    ┌──────────────┐
        keyboard ──►│ fd 0 stdin   │──► program
                    └──────────────┘
                    ┌──────────────┐
        program  ──►│ fd 1 stdout  │──► terminal
                    └──────────────┘
                    ┌──────────────┐
        program  ──►│ fd 2 stderr  │──► terminal / errors
                    └──────────────┘

        Examples:

            read(0, buffer, 10)      reads from stdin
            write(1, "OK\\n", 3)      writes normal output
            write(2, "Error\\n", 6)   writes an error message

        Why stderr exists:

            ./rush > out.txt
            stdout goes to out.txt
            stderr still appears in the terminal
        """,
        title="File Descriptors",
        style="magenta",
    )


def write_panel() -> Panel:
    return card(
        """
        write() = send bytes to a file descriptor

        Prototype:   write(fd, buffer, count);
        Example:     write(1, "Hello\\n", 6);

        ┌──────────┬──────────────┬────────────────────────────┐
        │ argument │ value        │ meaning                    │
        ├──────────┼──────────────┼────────────────────────────┤
        │ fd       │ 1            │ write to stdout            │
        │ buffer   │ "Hello\\n"    │ bytes to send              │
        │ count    │ 6            │ number of bytes to write   │
        └──────────┴──────────────┴────────────────────────────┘

        Visual:

        program
          │ write(1, "Hello\\n", 6)
          ▼
        fd 1 / stdout
          │
          ▼
        terminal  →  Hello

        [bold]Important:[/bold] write() does NOT care about strings, it only writes bytes.

            write(1, "Hello", 3);   → Hel
            write(1, "Hello", 5);   → Hello
            write(1, "Hello", 10);  → Hello + garbage risk

        Return value:   success → number of bytes written
                        error   → -1
        """,
        title="write()",
        style="green",
    )


def memory_panel() -> Panel:
    return card(
        """
        🏠 Imagine memory is a neighborhood.

        House A                 📮 Pointer P
        +---------+             +---------+
        |   42    |             | 0x1000  |
        +---------+             +---------+
        Address: 0x1000

        P doesn't store 42. P stores the address of House A.

                    +---------+
        P --------->| House A |
                    |   42    |
                    +---------+

        Reading it:

            a    = 42
            &a   = 0x1000
            p    = 0x1000
            *p   = 42     ← "Go to the house whose address is inside p."

        ──────────────────────────────────────

        Why use pointers?

            ✓ Modify variables inside functions
            ✓ Avoid copying large data
            ✓ Dynamic memory (malloc / free)
            ✓ Linked lists, trees, etc.

        ──────────────────────────────────────

        [bold]Golden rule[/bold]

            🏠 Variable  → stores a VALUE
            📮 Pointer   → stores an ADDRESS
            ⭐ *         → go to that address
        """,
        title="Pointers explained with houses",
        style="bright_magenta",
    )


def redirections_panel() -> Panel:
    return card(
        """
        [bold]NORMAL RUN[/bold]                 ./rush
            stdout ─────────► terminal
            stderr ─────────► terminal

        [bold]REDIRECT STDOUT[/bold]            ./rush > out.txt
            stdout ─────────► out.txt
            stderr ─────────► terminal

        [bold]REDIRECT STDERR[/bold]            ./rush 2> err.txt
            stdout ─────────► terminal
            stderr ─────────► err.txt

        [bold]REDIRECT BOTH[/bold]              ./rush > out.txt 2> err.txt
            stdout ─────────► out.txt
            stderr ─────────► err.txt
        """,
        title="Shell Redirections",
        style="bright_blue",
    )


def common_mistakes_panel() -> Panel:
    return card(
        """
        [bold]1. Using argv[1] without checking argc[/bold]

            printf("%s\\n", argv[1]);     run: ./rush
            → argc == 1, so argv[1] == NULL

        ──────────────────────────────────────────────

        [bold]2. Thinking argv[0] is the first user argument[/bold]

            ./rush hello
            argv[0] = "./rush"
            argv[1] = "hello"

        ──────────────────────────────────────────────

        [bold]3. Wrong write count[/bold]

            write(1, "Hello", 10);
            → write() writes exactly 10 bytes. It does not stop at '\\0'.

        ──────────────────────────────────────────────

        [bold]4. Using sizeof on a pointer[/bold]

            char *str = "Hello";
            sizeof(str)
            → pointer size, not string length.
        """,
        title="Common Mistakes",
        style="red",
    )
