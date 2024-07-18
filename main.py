import sys
from cli import ToDoListCLI
from gui import ToDoListGUI
import tkinter as tk

def main():
    while True:
        check = int(input("Enter the number of command:\n1.GUI\n2.CLI\n0.Exit\n"))
        if check == 2:
            cli_app = ToDoListCLI()
            cli_app.run()
        elif check == 1:
            root = tk.Tk()
            gui_app = ToDoListGUI(root)
            root.mainloop()
        elif check == 0:
            break;
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()

