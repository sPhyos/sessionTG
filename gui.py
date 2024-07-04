import tkinter as tk
from tkinter import messagebox
from todo import ToDoList

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.todo_list = ToDoList()
        
        self.frame = tk.Frame(root)
        self.frame.pack()
        
        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=10)
        
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10)
        
        self.tasks_listbox = tk.Listbox(root, width=50, height=15)
        self.tasks_listbox.pack(padx=10, pady=10)
        
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.todo_list.add_task(task)
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.tasks_listbox.delete(selected_task_index)
            self.todo_list.remove_task(selected_task_index[0])
        else:
            messagebox.showwarning("Warning", "You must select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()
