import datetime

class Task:
    def __init__(self, title: str, date_due: datetime.datetime):
        self.title = title
        self.date_created = datetime.datetime.now()
        self.completed = False
        self.date_due = date_due

    def change_title(self, new_title: str) -> None:
        self.title = new_title

    def change_date_due(self, date_due: datetime.datetime) -> None:
        self.date_due = date_due

    def mark_completed(self) -> None:
        self.completed = True

    def __str__(self) -> str:
        return f"{self.title} | Due: {self.date_due.date()} | Completed: {self.completed}"


class RecurringTask(Task):
    def __init__(self, title: str, date_due: datetime.datetime, interval: datetime.timedelta):
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates: list[datetime.datetime] = []

    def _compute_next_due_date(self) -> datetime.datetime:
        return self.date_due + self.interval

    def mark_completed(self) -> None:
        self.completed_dates.append(datetime.datetime.now())
        self.date_due = self._compute_next_due_date()

    def __str__(self) -> str:
        return f"{self.title} (Recurring every {self.interval.days} days) | Next due: {self.date_due.date()}"