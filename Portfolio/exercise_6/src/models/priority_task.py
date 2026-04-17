from models.task import Task
import datetime
from typing import Dict

# OCP + LSP: Extends Task with priority functionality
# Can be used wherever Task is used
class PriorityTask(Task):
    # Mapping from priority level to string representation
    PRIORITY_LEVELS: Dict[int, str] = {
        1: "low",
        2: "medium",
        3: "high"
    }
    
    def __init__(self, title: str, date: datetime.datetime, priority: int) -> None:
        """
        Initialize a PriorityTask.
        
        Args:
            title: The task title
            date: The due date for the task
            priority: Priority level (1-3 where 1=low, 2=medium, 3=high)
            
        Raises:
            ValueError: If priority is not between 1 and 3
        """
        super().__init__(title, date)
        
        # Validate priority level
        if priority not in self.PRIORITY_LEVELS:
            raise ValueError(f"Priority must be between 1 and 3, got {priority}")
        
        self._priority = priority

    @property
    def priority(self) -> int:
        """Get the priority level."""
        return self._priority
    
    @priority.setter
    def priority(self, value: int) -> None:
        """Set the priority level with validation."""
        if value not in self.PRIORITY_LEVELS:
            raise ValueError(f"Priority must be between 1 and 3, got {value}")
        self._priority = value

    def get_priority_string(self) -> str:
        """
        Get the string representation of the priority level.
        
        Returns:
            The priority level as a string ('low', 'medium', or 'high')
        """
        return self.PRIORITY_LEVELS[self._priority]

    def __str__(self) -> str:
        status = "Done" if self.completed else "Pending"
        priority_str = self.get_priority_string()
        return f"[{priority_str.upper()}] {self.title} | Due: {self.date.date()} | {status}"
