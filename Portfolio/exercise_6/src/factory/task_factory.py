from models.task import Task
from models.recurring_task import RecurringTask
from models.priority_task import PriorityTask
import datetime
from typing import Optional

# Factory Pattern + DIP: Handles object creation
class TaskFactory:
    @staticmethod
    def create_task(title: str, date: datetime.datetime, **kwargs) -> Task:
        """
        Create a task based on provided parameters.
        
        Args:
            title: The task title
            date: The due date
            **kwargs: Optional keyword arguments:
                - interval: timedelta for recurring tasks
                - priority: int (1-3) for priority tasks
                
        Returns:
            Task: A Task, RecurringTask, or PriorityTask instance
        """
        # OCP: Can extend with new task types easily
        
        if "priority" in kwargs:
            priority = kwargs["priority"]
            return PriorityTask(title, date, priority)
        
        if "interval" in kwargs:
            return RecurringTask(title, date, kwargs["interval"])
        
        return Task(title, date)
