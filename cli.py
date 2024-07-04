from todo import ToDoList

class ToDoListCLI:
    def __init__(self):
        self.todo_list = ToDoList()
    
    def run(self):
        while True:
            command = int(input("Enter number of command (1. Add\t2. Remove\t3. List,4. Quit): ").strip().lower())
            if command == 1:
                task = input("Enter a task: ").strip()
                self.todo_list.add_task(task)
                print(f"Task '{task}' added")
            elif command == 2:
                task = int(input("Enter task number to remove: "))
                removed_task = self.todo_list.remove_task(task)
                if removed_task:
                    print(f"Task '{removed_task}' removed")
                else:
                    print("Invalid task number")
            elif command == 3:
                tasks = self.todo_list.list_tasks()
                if not tasks:
                    print("No tasks in the to-do list")
                else:
                    for i , task in enumerate(tasks):
                        print(f"{i + 1}. {task} ")
            elif command == 4:
                print("Exiting the to-do list application.")
                break
            else:
                print("Enter valid command number.")