# SRP: Manages the collection of tasks ONLY
class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_task(self, index):
        return self.tasks[index]

    # DRY + validation logic reused across app
    def check_task_index(self, ix: int) -> bool:
        return 0 <= ix < len(self.tasks)