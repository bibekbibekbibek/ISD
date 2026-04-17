from models.task_list import TaskList
from factory.task_factory import TaskFactory
import datetime

# SRP: Handles business logic ONLY (no UI here)
class TaskManagerController:
    def __init__(self):
        # DIP: Uses abstraction (TaskList) instead of raw list
        self.task_list = TaskList()

    def add_task(self, title, days):
        date = datetime.datetime.now() + datetime.timedelta(days=days)
        
        # Factory Pattern used (no direct Task creation)
        task = TaskFactory.create_task(title, date)
        self.task_list.add_task(task)

    def add_recurring_task(self, title, days, interval_days):
        date = datetime.datetime.now() + datetime.timedelta(days=days)
        interval = datetime.timedelta(days=interval_days)

        # Creates RecurringTask via factory
        task = TaskFactory.create_task(title, date, interval=interval)
        self.task_list.add_task(task)

    def complete_task(self, index):
        # Uses TaskList validation (DRY principle)
        if self.task_list.check_task_index(index):
            task = self.task_list.get_task(index)
            
            # LSP: Works for both Task and RecurringTask
            task.mark_completed()
            return True
        return False

    def delete_task(self, index):
        if self.task_list.check_task_index(index):
            self.task_list.tasks.pop(index)
            return True
        return False

    def get_all_tasks(self):
        return self.task_list.tasks