class Task:
    def __init__(self, title, due_date, description=""):
        self.title = title
        self.due_date = due_date
        self.description = description

    def change_title(self, new_title):
        self.title = new_title

    def change_due_date(self, new_due_date):
        self.due_date = new_due_date

    def change_description(self, new_description):
        self.description = new_description

    def __str__(self):
        return f"Title: {self.title}\nDue Date: {self.due_date}\nDescription: {self.description}"
    
    