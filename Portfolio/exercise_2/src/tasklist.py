from datetime import datetime

class TaskList:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if 0 <= task < len(self.tasks):
            del self.tasks[task]
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks in the list.")
        else:
            for index, task in enumerate(self.tasks):
                print(f"Task {index + 1}:\n{task}\n")
                
    def edit_task(self, task_index, new_title=None, new_due_date=None, new_description=None):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            if new_title is not None:
                task.change_title(new_title)
            if new_due_date is not None:
                task.change_due_date(new_due_date)
            if new_description is not None:
                task.change_description(new_description)
        else:
            print("Invalid task index.")

    def list_options(self):
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Edit Task")
        print("5. View Overdue Tasks")
        print("6. Exit")

    def view_overdue_tasks(self):
        current_date = datetime.now()
        found = False
        for task in self.tasks:
            if task.due_date < current_date and not task.completed:
                print(task)
                found = True

        if not found:
            print("No overdue tasks found.")