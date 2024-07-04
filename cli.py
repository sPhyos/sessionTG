from todo import ToDoList

class ToDoListCLI:
    def __init__(self):
        self.todo_list = ToDoList()

    def run(self):
        while True:
            command = input("Enter command (add, remove, list, quit): ").strip().lower()
            if command == "add":
                task = input("Enter a task: ").strip()
                self.todo_list.add_task(task)
                print(f"Task '{task}' added.")
            elif command == "remove":
                task_number = int(input("Enter task number to remove: ").strip()) - 1
                removed_task = self.todo_list.remove_task(task_number)
                if removed_task:
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
            elif command == "list":
                tasks = self.todo_list.list_tasks()
                if not tasks:
                    print("No tasks in the to-do list.")
                else:
                    print("To-Do List:")
                    for i, task in enumerate(tasks):
                        print(f"{i + 1}. {task}")
            elif command == "quit":
                print("Exiting the to-do list application.")
                break
            else:
                print("Unknown command.")
