import sys
from cli import ToDoListCLI
from gui import ToDoListGUI
import tkinter as tk

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        cli_app = ToDoListCLI()
        cli_app.run()
    else:
        root = tk.Tk()
        gui_app = ToDoListGUI(root)
        root.mainloop()

if __name__ == "__main__":
    main()

