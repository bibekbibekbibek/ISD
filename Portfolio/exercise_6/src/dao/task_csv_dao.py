"""
Data Access Object (DAO) for persisting tasks to CSV
Supports Task, RecurringTask, and PriorityTask
"""

import csv
import datetime
from typing import List
from models.task import Task
from models.recurring_task import RecurringTask
from models.priority_task import PriorityTask

class TaskCsvDAO:
    """Data access object for saving and loading tasks from CSV."""
    
    def __init__(self, storage_path: str) -> None:
        """
        Initialize the DAO with a CSV file path.
        
        Args:
            storage_path: Path to the CSV file for task storage
        """
        self.storage_path = storage_path
        self.fieldnames = [
            "title", 
            "type", 
            "date_due", 
            "completed", 
            "interval",
            "priority"
        ]

    def get_all_tasks(self) -> List[Task]:
        """
        Load all tasks from the CSV file.
        
        Returns:
            A list of Task, RecurringTask, or PriorityTask objects
        """
        task_list: List[Task] = []
        
        try:
            with open(self.storage_path, "r") as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    task_type = row.get("type", "Task").strip()
                    title = row.get("title", "").strip()
                    date_due_str = row.get("date_due", "")
                    completed = row.get("completed", "False").lower() == "true"
                    
                    # Parse the date
                    try:
                        task_date = datetime.datetime.strptime(date_due_str, "%Y-%m-%d %H:%M:%S.%f")
                    except ValueError:
                        try:
                            task_date = datetime.datetime.strptime(date_due_str, "%Y-%m-%d")
                        except ValueError:
                            task_date = datetime.datetime.now()
                    
                    # Create the appropriate task type
                    if task_type == "RecurringTask":
                        interval_str = row.get("interval", "7").strip()
                        try:
                            interval_days = int(interval_str)
                        except ValueError:
                            interval_days = 7
                        
                        task = RecurringTask(title, task_date, datetime.timedelta(days=interval_days))
                    
                    elif task_type == "PriorityTask":
                        priority_str = row.get("priority", "1").strip()
                        try:
                            priority = int(priority_str)
                        except ValueError:
                            priority = 1
                        
                        task = PriorityTask(title, task_date, priority)
                    
                    else:
                        task = Task(title, task_date)
                    
                    # Set completion status
                    if completed:
                        task.completed = True
                    
                    task_list.append(task)
        
        except FileNotFoundError:
            # File doesn't exist yet, return empty list
            pass
        
        return task_list

    def save_all_tasks(self, tasks: List[Task]) -> bool:
        """
        Save all tasks to the CSV file.
        
        Args:
            tasks: List of tasks to save
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(self.storage_path, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
                
                for task in tasks:
                    row = {
                        "title": task.title,
                        "type": type(task).__name__,
                        "date_due": task.date.strftime("%Y-%m-%d %H:%M:%S.%f"),
                        "completed": str(task.completed),
                        "interval": "",
                        "priority": ""
                    }
                    
                    # Add type-specific fields
                    if isinstance(task, RecurringTask):
                        row["interval"] = str(task.interval.days)
                    
                    elif isinstance(task, PriorityTask):
                        row["priority"] = str(task.priority)
                    
                    writer.writerow(row)
            
            return True
        
        except Exception as e:
            print(f"Error saving tasks to CSV: {e}")
            return False
