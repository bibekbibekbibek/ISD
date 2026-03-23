import datetime
from tasks import Task


class TaskList:

    def __init__(self, owner: str):
        self.owner = owner
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, ix: int):
        if 0 <= ix < len(self.tasks):
            self.tasks.pop(ix)
        else:
            print("Task not found.")

    def get_task(self, ix: int):
        if 0 <= ix < len(self.tasks):
            return self.tasks[ix]
        else:
            print("Task not found.")
            return None

    def view_tasks(self):

        if not self.tasks:
            print("No tasks available.")
            return

        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def list_options(self):
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. View Overdue Tasks")
        print("5. Mark Task as Completed")
        print("6. Exit")

    def view_overdue_tasks(self):

        today = datetime.date.today()

        overdue_tasks = [
            task for task in self.tasks
            if task.due_date < today and not task.completed
        ]

        if overdue_tasks:
            print("\nOverdue Tasks:")
            for task in overdue_tasks:
                print(task)
        else:
            print("No overdue tasks.")



from tasks import Task

class TaskList:

    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task index.")

    def get_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        else:
            print("Invalid task index.")
            return None
        
    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Pending"
                print(f"{i}. {task.description} - {status}")