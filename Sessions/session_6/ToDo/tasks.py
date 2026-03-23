import datetime

class Task:
    def __init__(self, title: str, description: str, due_date: datetime.date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.title} | Due: {self.due_date} | {status}"


class RecurringTask(Task):
    def __init__(self, title, description, due_date, interval):
        super().__init__(title, description, due_date)
        self.interval = interval

    def mark_completed(self):
        # Move to next due date instead of finishing
        self.due_date += self.interval

    def __str__(self):
        return f"{self.title} (Recurring) | Due: {self.due_date}"