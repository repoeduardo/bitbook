import config
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich import inspect
#inspect(my_list, methods=True)

class Menu:

    def main_menu(self):
        console = Console()
        n = 10
        print(Panel("Imprime texto [red]formatado? {n}"))
        print(Panel("0 - Exit \n1 - Book list \n2 - New book\n3 - Delete book", title="MAIN MENU"))
        r = console.input("[green]> ")
        print(r)
