from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree
from rich.align import Align


def argv_table(command: str) -> Table:
    """
    Build a Rich table representing argc and argv.
    """

    argv = command.split()
    argc = len(argv)

    table = Table(
        title=f"Command: {command}",
        border_style="cyan",
        show_lines=True,
        expand=True,
    )

    table.add_column("Index", justify="center", style="bold cyan")
    table.add_column("Value", style="yellow")
    table.add_column("Type", justify="center", style="green")

    for i, arg in enumerate(argv):
        table.add_row(
            f"argv[{i}]",
            f'"{arg}"',
            "char *"
        )

    table.add_row(
        f"argv[{argc}]",
        "[bold red]NULL[/bold red]",
        "End"
    )

    return table

def argv_tree(command: str) -> Tree:
    """
    Draw argv as a pointer tree.
    """

    argv = command.split()

    tree = Tree("[bold cyan]argv[/bold cyan]")

    for i, arg in enumerate(argv):
        tree.add(f'argv[{i}] → "{arg}"')

    tree.add("[bold red]argv[argc] → NULL[/bold red]")

    return tree


def fd_panel() -> Panel:
    """
    Standard file descriptors.
    """

    text = """
    FILE DESCRIPTORS = numbers used by the OS to access streams

    When a program starts, it already has 3 open doors:

    ┌───────────────┬──────────┬────────────────────────────┐
    │ FD number     │ Name     │ Usually connected to       │
    ├───────────────┼──────────┼────────────────────────────┤
    │ 0             │ stdin    │ keyboard / input           │
    │ 1             │ stdout   │ terminal / normal output   │
    │ 2             │ stderr   │ terminal / error output    │
    └───────────────┴──────────┴────────────────────────────┘


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

    read(0, buffer, 10)
        reads from stdin

    write(1, "OK\n", 3)
        writes normal output

    write(2, "Error\n", 6)
        writes an error message


    Why stderr exists:

    ./rush > out.txt

    stdout goes to out.txt
    stderr still appears in the terminal
    """
    return Panel(
    Align.center(text),
    title="File Descriptors",
    border_style="magenta",
    )


def write_panel() -> Panel:
    """
    Explain write().
    """

    drawing = r"""
    write() = send bytes to a file descriptor

    Prototype:

        write(fd, buffer, count);

    Example:

        write(1, "Hello\n", 6);


    What each argument means:

    ┌──────────┬──────────────┬────────────────────────────┐
    │ argument │ value        │ meaning                    │
    ├──────────┼──────────────┼────────────────────────────┤
    │ fd       │ 1            │ write to stdout            │
    │ buffer   │ "Hello\n"    │ bytes to send              │
    │ count    │ 6            │ number of bytes to write   │
    └──────────┴──────────────┴────────────────────────────┘


    Visual:

    program
      │
      │ write(1, "Hello\n", 6)
      ▼
    fd 1 / stdout
      │
      ▼
    terminal

    Output:

        Hello


    Important:

    write() does NOT care about strings.
    write() only writes bytes.

    So:

        write(1, "Hello", 3);   → Hel
        write(1, "Hello", 5);   → Hello
        write(1, "Hello", 10);  → Hello + garbage risk


    Return value:

        success → number of bytes written
        error   → -1
    """

    return Panel(
        drawing,
        title="write()",
        border_style="green",
    )

def memory_panel() -> Panel:
    """
    Explain argv memory.
    """

    drawing = r"""
    🏠 Imagine memory is a neighborhood.

    House A
    +---------+
    |   42    |
    +---------+
    Address: 0x1000

    📮 Pointer P

    +---------+
    | 0x1000  |
    +---------+

    P doesn't store 42.
    P stores the address of House A.

                +---------+
    P --------->| House A |
                |   42    |
                +---------+

    Reading it:

    a      = 42

    &p     ❌ (address of p)

    &a     = 0x1000

    p      = 0x1000

    *p     = 42
              ↑
         "Go to the house
          whose address is
          inside p."

    ──────────────────────────────────────

    Why use pointers?

    ✓ Modify variables inside functions

    ✓ Avoid copying large data

    ✓ Dynamic memory (malloc / free)

    ✓ Linked lists, trees, etc.

    ──────────────────────────────────────

    Golden rule

    🏠 Variable  → stores a VALUE

    📮 Pointer   → stores an ADDRESS

    ⭐ *          → go to that address
    """

    return Panel(
        drawing,
        title="Pointers explained with houses",
        border_style="bright_magenta",
    )

def redirections_panel() -> Panel:
    drawing = r"""
    NORMAL RUN

        ./rush

    stdout ─────────► terminal
    stderr ─────────► terminal


    REDIRECT STDOUT

        ./rush > out.txt

    stdout ─────────► out.txt
    stderr ─────────► terminal


    REDIRECT STDERR

        ./rush 2> err.txt

    stdout ─────────► terminal
    stderr ─────────► err.txt


    REDIRECT BOTH

        ./rush > out.txt 2> err.txt

    stdout ─────────► out.txt
    stderr ─────────► err.txt
    """

    return Panel(
        drawing,
        title="Shell Redirections",
        border_style="bright_blue",
    )

def common_mistakes_panel() -> Panel:
    drawing = r"""
    1. Using argv[1] without checking argc

        printf("%s\n", argv[1]);

    Run:

        ./rush

    Problem:

        argc == 1
        argv[1] == NULL


    ──────────────────────────────────────────────

    2. Thinking argv[0] is the first user argument

        ./rush hello

        argv[0] = "./rush"
        argv[1] = "hello"


    ──────────────────────────────────────────────

    3. Wrong write count

        write(1, "Hello", 10);

    Problem:

        write() writes exactly 10 bytes.
        It does not stop at '\0'.


    ──────────────────────────────────────────────

    4. Using sizeof on a pointer

        char *str = "Hello";
        sizeof(str)

    Problem:

        sizeof(str) = pointer size, not string length.
    """

    return Panel(drawing, title="Common Mistakes", border_style="red")
