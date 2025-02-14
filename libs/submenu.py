from 'menu' import Menu
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table

class Submenu(Menu):

    def submenu_update_book():
        console = Console()
        print(Panel("0 - Main menu \n1 - Update by id \n2 - Update by name\n3 - Delete book\n4 - Update book\n5 - Help", title="MAIN MENU"))
