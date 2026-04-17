from models.task import Task
import datetime

# OCP + LSP: Extends Task without modifying it
# Can be used wherever Task is used
class RecurringTask(Task):
    def __init__(self, title: str, date: datetime.datetime, interval: datetime.timedelta):
        super().__init__(title, date)
        self.interval = interval

    def mark_completed(self) -> None:
        # Different behaviour: instead of completing,
        # move the task forward (recurring logic)
        self.date += self.interval

    def __str__(self) -> str:
        status = "Done" if self.completed else "Pending"
        return f"{self.title} | Due: {self.date.date()} | Repeats every {self.interval.days} days | {status}"
