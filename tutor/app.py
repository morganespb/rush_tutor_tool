from rich.prompt import Prompt
from tutor.simulator import simulator_screen
from tutor.screens import home_screen, argc_argv_screen, memory_screen, fd_screen, write_screen, redirections_screen, common_mistakes_screen, goodbye_screen
from tutor.code_cases import code_cases_screen
from tutor.memory_simulator import memory_simulator_screen
from tutor.argv_playground import argv_playground_screen


from tutor import screens, utils
from tutor.utils import console

def clear() -> None:
    console.clear()

#def show_home() -> str:
#    clear()
#
#    console.print(
#        Panel(
#            "[bold yellow]RUSH00 TUTOR TOOL[/bold yellow]\n\n"
#            "[cyan]Outil de présentation pour expliquer :[/cyan]\n\n"
#            "1. argc / argv\n"
#            "2. Visualisation mémoire\n"
#            "3. File descriptors\n"
#            "4. write()\n"
#            "5. Redirections\n"
#            "6. Erreurs classiques\n"
#            "7. Simulateur argc/argv\n"
#            "8. Questions d'évaluation\n\n"
#            "[dim]q. quitter[/dim]",
#            title="42 Tutor Mode",
#            border_style="yellow",
#        )
#    )
#
#    return Prompt.ask(
#        "\nChoix",
#        choices=["1", "2", "3", "4", "5", "6", "7", "8", "q"],
#    )


def placeholder(title: str) -> None:
    clear()
    console.print(
        Panel(
            f"[bold green]{title}[/bold green]\n\n"
            "Cette section arrive à l'étape suivante.",
            border_style="green",
        )
    )
    pause()

SCREENS = {
    "1": argc_argv_screen,
    "2": memory_screen,
    "3": fd_screen,
    "4": write_screen,
    "5": redirections_screen,
    "6": common_mistakes_screen,
    "7": simulator_screen,
    "8": code_cases_screen,
    "9": memory_simulator_screen,
    "10": argv_playground_screen,
}
ORDER = list(SCREENS)


def run() -> None:
    # Full-screen mode: the terminal is restored as it was when you quit.
    with console.screen():
        try:
            choice = home_screen()
            while choice != "q":
                utils.last_key = None
                SCREENS[choice]()

                # ← / → after a lesson flips to the previous / next one, like slides.
                step = {"left": -1, "right": 1}.get(utils.last_key)
                if step:
                    choice = ORDER[(ORDER.index(choice) + step) % len(ORDER)]
                    screens.selected = ORDER.index(choice)
                else:
                    choice = home_screen()

            goodbye_screen()
        except (KeyboardInterrupt, EOFError):
            pass
