import datetime
from typing import Optional

# SRP: This class is ONLY responsible for storing task data
class Task:
    def __init__(self, title: str, date: datetime.datetime):
        self.title = title
        self.date = date
        self.completed = False

    def mark_completed(self) -> None:
        # Marks task as completed
        self.completed = True

    def __str__(self) -> str:
        status = "Done" if self.completed else "Pending"
        return f"{self.title} | Due: {self.date.date()} | {status}"
