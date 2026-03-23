import datetime


class Task:

    def __init__(self, title: str, description: str, due_date: datetime.date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.date_created = datetime.datetime.now()

    def mark_completed(self):
        self.completed = True

    def change_title(self, new_title: str):
        self.title = new_title

    def change_description(self, new_description: str):
        self.description = new_description

    def change_due_date(self, new_due_date: datetime.date):
        self.due_date = new_due_date

    def __str__(self):
        return f"{self.title} | Due: {self.due_date} | Completed: {self.completed}"


class RecurringTask(Task):

    def __init__(self, title: str, description: str, due_date: datetime.date, interval: datetime.timedelta):
        super().__init__(title, description, due_date)
        self.interval = interval
        self.completed_dates = []

    def _compute_next_due_date(self):
        return self.due_date + self.interval

    def mark_completed(self):

        current_date = datetime.datetime.now()
        self.completed_dates.append(current_date)

        self.due_date = self._compute_next_due_date()

    def __str__(self):
        completed = ", ".join([d.strftime("%Y-%m-%d") for d in self.completed_dates])
        return f"{self.title} (Recurring) | Due: {self.due_date} | Completed dates: {completed}"



class Task:

    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.description} [{status}]"