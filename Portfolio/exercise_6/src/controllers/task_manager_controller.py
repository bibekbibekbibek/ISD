from models.task_list import TaskList
from factory.task_factory import TaskFactory
import datetime

# SRP: Handles business logic ONLY (no UI here)
class TaskManagerController:
    def __init__(self) -> None:
        # DIP: Uses abstraction (TaskList) instead of raw list
        self.task_list = TaskList()

    def add_task(self, title: str, days: int) -> bool:
        """Add a regular task."""
        try:
            date = datetime.datetime.now() + datetime.timedelta(days=days)
            
            # Factory Pattern used (no direct Task creation)
            task = TaskFactory.create_task(title, date)
            self.task_list.add_task(task)
            return True
        except Exception as e:
            print(f"Error adding task: {e}")
            return False

    def add_recurring_task(self, title: str, days: int, interval_days: int) -> bool:
        """Add a recurring task."""
        try:
            date = datetime.datetime.now() + datetime.timedelta(days=days)
            interval = datetime.timedelta(days=interval_days)

            # Creates RecurringTask via factory
            task = TaskFactory.create_task(title, date, interval=interval)
            self.task_list.add_task(task)
            return True
        except Exception as e:
            print(f"Error adding recurring task: {e}")
            return False

    def add_priority_task(self, title: str, days: int, priority: int) -> bool:
        """Add a priority task."""
        try:
            date = datetime.datetime.now() + datetime.timedelta(days=days)
            
            # Creates PriorityTask via factory
            task = TaskFactory.create_task(title, date, priority=priority)
            self.task_list.add_task(task)
            return True
        except ValueError as e:
            print(f"Invalid priority: {e}")
            return False
        except Exception as e:
            print(f"Error adding priority task: {e}")
            return False

    def complete_task(self, index: int) -> bool:
        """Mark a task as completed."""
        # Uses TaskList validation (DRY principle)
        if self.task_list.check_task_index(index):
            task = self.task_list.get_task(index)
            
            # LSP: Works for Task, RecurringTask, and PriorityTask
            task.mark_completed()
            return True
        return False

    def delete_task(self, index: int) -> bool:
        """Delete a task."""
        if self.task_list.check_task_index(index):
            self.task_list.tasks.pop(index)
            return True
        return False

    def get_all_tasks(self):
        """Get all tasks."""
        return self.task_list.tasks
