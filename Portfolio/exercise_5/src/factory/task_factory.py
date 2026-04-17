from models.task import Task
from models.recurring_task import RecurringTask

# Factory Pattern + DIP: Handles object creation
class TaskFactory:
    @staticmethod
    def create_task(title, date, **kwargs):
        # OCP: Can extend with new task types easily
        if "interval" in kwargs:
            return RecurringTask(title, date, kwargs["interval"])
        return Task(title, date)