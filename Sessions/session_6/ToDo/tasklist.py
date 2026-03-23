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
            print("Task not found")

    def get_task(self, ix: int):
        if 0 <= ix < len(self.tasks):
            return self.tasks[ix]
        return None

    @property
    def uncompleted_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def view_tasks(self):
        print("The following tasks are still to be done:")

        if not self.uncompleted_tasks:
            print("No remaining tasks")
            return

        for task in self.uncompleted_tasks:
            ix = self.tasks.index(task)
            print(f"{ix}: {task}")