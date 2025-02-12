import config
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich import inspect
#inspect(my_list, methods=True)

class Menu:

    def main_menu(self):
        console = Console()
        print(Panel("[yellow]BITBOOK :book:"))
        print(Panel("0 - Exit \n1 - Book list \n2 - New book\n3 - Delete book\n4 - Update book\n5 - Help", title="MAIN MENU"))

        while True:
            menu_option = str(console.input("[green]> ")).strip()  # Removes extra spaces

            if menu_option.isdigit() and 0 <= int(menu_option) <= 5:  # Checks if it's a number and within the range
                menu_option = int(menu_option)  # Converts to integer
                break  # Exits the loop if valid
            else:
                console.print("[red]Invalid input! Please enter numbers within the option range (0 - 5).[/red]")

        print(f"Selected option: {menu_option}")  # Example output for verification
        return menu_option

    def book_list(self):
        print(f"listing books...")

    def new_book(self):
        print(f"New books...")

    def delete_book(self):
        print(f"Delete books...")

    def update_book(self):
        print(f"Update books...")

    def help(self):
        print(f" Help...")
