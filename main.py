from models.books import Book
from libs.menu import Menu
from rich import print
from rich.panel import Panel

execution = True

print("\n[yellow]WELCOME TO BITBOOK - BOOK MANAGER")
while execution:
    menu = Menu()

    menu_option = menu.main_menu()

    match (menu_option):
        case 0:
            execution = False
        case 1:
            menu.book_list()
        case 2:
            menu.new_book()
        case 3:
            menu.delete_book()
        case 4:
            menu.update_book()
        case _:
            print("menu_option invalid")
