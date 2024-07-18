import sys
from cli import ToDoListCLI
from gui import ToDoListGUI
import tkinter as tk

def show_menu():
    print("\nWelcome to the To-Do List Application!")
    print("Please select an option:")
    print("1. GUI")
    print("2. CLI")
    print("0. Exit")

def get_user_choice():
    try:
        return int(input("Enter the number of your choice: "))
    except ValueError:
        return -1

def run_cli():
    cli_app = ToDoListCLI()
    cli_app.run()

def run_gui():
    root = tk.Tk()
    gui_app = ToDoListGUI(root)
    root.mainloop()

def main():
    while True:
        show_menu()
        choice = get_user_choice()
        if choice == 2:
            run_cli()
        elif choice == 1:
            run_gui()
        elif choice == 0:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Unknown command. Please enter a valid option.")

if __name__ == "__main__":
    main()
