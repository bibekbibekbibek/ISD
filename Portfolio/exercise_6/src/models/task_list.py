from models.task import Task
from typing import List

# SRP: Responsible for managing the collection of tasks
class TaskList:
    def __init__(self) -> None:
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to the list."""
        self.tasks.append(task)

    def check_task_index(self, index: int) -> bool:
        """Check if a task index is valid."""
        return 0 <= index < len(self.tasks)

    def get_task(self, index: int) -> Task:
        """Get a task by index."""
        if self.check_task_index(index):
            return self.tasks[index]
        raise IndexError(f"Task index {index} out of range")
