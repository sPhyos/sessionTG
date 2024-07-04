class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            return self.tasks.pop(task_number)
        return None

    def list_tasks(self):
        return self.tasks
