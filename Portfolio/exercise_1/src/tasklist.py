from tasks import Task

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if 0 <= task < len(self.tasks):
            del self.tasks[task]
        else:
            print("Invalid task index.")

    def show_tasks(self):
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