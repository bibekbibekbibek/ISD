from typing import List
from tasks import Task


class TaskList:
    def __init__(self) -> None:
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, index: int) -> None:
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid index")

    def get_task(self, index: int) -> Task | None:
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    def display_tasks(self) -> None:
        if not self.tasks:
            print("No tasks available.")
            return

        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")