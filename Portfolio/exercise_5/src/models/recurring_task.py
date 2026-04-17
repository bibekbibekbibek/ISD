from models.task import Task
import datetime

# OCP + LSP: Extends Task without modifying it
# Can be used wherever Task is used
class RecurringTask(Task):
    def __init__(self, title, date, interval):
        super().__init__(title, date)
        self.interval = interval

    def mark_completed(self):
        # Different behaviour: instead of completing,
        # move the task forward (recurring logic)
        self.date += self.interval