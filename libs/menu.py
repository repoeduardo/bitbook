import config
from models.books import Book
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.table import Table
from rich import inspect
#inspect(my_list, methods=True)

class Menu:

    def main_menu(self):
        console = Console()
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
        book = Book()
        console = Console()

        list_of_all_books = book.select_all()

        # Criar uma tabela
        table = Table(title="Catalogue")

        # Adicionar colunas na tabela, correspondendo aos campos do banco de dados
        table.add_column("ID", style="cyan", no_wrap=True)
        table.add_column("Author", style="magenta")
        table.add_column("Title", style="green")
        table.add_column("Subtitle", style="yellow")
        table.add_column("Genre", style="blue")
        table.add_column("Year", style="red")
        table.add_column("Publisher", style="white")
        table.add_column("Description", style="cyan")

        # Preencher a tabela com os dados
        for row in list_of_all_books:
            table.add_row(str(row[0]), row[1], row[2], row[3], row[4], str(row[5]), row[6], row[7])

        console.print(table)

    def new_book(self):
        console = Console()

        while True: # AUTHOR - REQUIRED
            console.print("\n[yellow]required[/yellow]")
            author = str(console.input("[cyan]Type author of the book > ")).strip()  # Removes extra spaces
            if not author:
                console.print("[red]The author field cannot be empty. Please enter an author name.[/red]")
            else:
                console.print("[green]registered successfully[/green]")
                break

        while True: # TITLE - REQUIRED
            console.print("\n[yellow]required[/yellow]")
            title = str(console.input("[cyan]Type title of the book > ")).strip()  # Removes extra spaces
            if not title:
                console.print("[red]The title field cannot be empty. Please enter the title of the book.[/red]")
            else:
                console.print("[green]registered successfully[/green]")
                break

        # SUBTITLE - OPTIONAL
        console.print("\n[bright_black]optional (keep blank to skip)[/bright_black]")
        subtitle = str(console.input("[cyan]Type subtitle of the book > ")).strip()  # Removes extra spaces
        if not subtitle:
            subtitle = ''


        while True: # GENRE - REQUIRED
            console.print("\n[yellow]required[/yellow]")
            genre = str(console.input("[cyan]Type genre of the book > ")).strip()  # Removes extra spaces
            if not genre:
                console.print("[red]The genre field cannot be empty. Please enter the genre of the book.[/red]")
            else:
                console.print("[green]registered successfully[/green]")
                break

        while True: # BOOK YEAR - REQUIRED
            console.print("\n[yellow]required[/yellow]")
            book_year = str(console.input("[cyan]Type publication year > ")).strip()  # Removes extra spaces

            if book_year and book_year.isdigit():
                book_year = int(book_year)
                console.print("[green]registered successfully[/green]")
                break
            else:
                console.print("[red]The publication year field cannot be empty and must contain only numbers.[/red]")


        while True: # PUBLISHER - REQUIRED
            console.print("\n[yellow]required[/yellow]")
            publisher = str(console.input("[cyan]Type publisher of the book > ")).strip()  # Removes extra spaces
            if not publisher:
                console.print("[red]The publisher field cannot be empty. Please enter the publisher of the book.[/red]")
            else:
                console.print("[green]registered successfully[/green]")
                break

        # DESCRIPTION - OPTIONAL
        console.print("\n[bright_black]optional (keep blank to skip)[/bright_black]")
        book_description = str(console.input("[cyan]Type description of the book > ")).strip()  # Removes extra spaces
        if not book_description:
            book_description = ''

        book = Book(author, title, subtitle, genre, book_year, publisher, book_description)
        book.insert()
        self.book_list()

        #print(f"\n Author: {author}\t Title: {title}\t Subtitle: {subtitle}\t Genre: {genre}\t Year: {book_year}\t Publisher: {publisher}\t Desc: {book_description}")

    def delete_book(self):
        console = Console()
        book = Book()
        while True:
            #console.print("\n[yellow]required[/yellow]")
            book_id = str(console.input("[cyan]Type the book ID > ")).strip()  # Removes extra spaces

            if book_id and book_id.isdigit() and book.this_id_exist(book_id):
                book_id = int(book_id)
                break
            else:
                console.print("[red]The field cannot be empty and must contain a valid book ID.[/red]\n")

        book.delete_by_id(book_id)
        self.book_list()

    def update_book(self):
        print(f"Update books...")

    def help(self):
        print(f" Help...")
