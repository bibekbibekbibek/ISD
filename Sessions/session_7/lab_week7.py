# Exception Handling (Exercise 6)
from datetime import datetime, timedelta


def complete_task(self, ix):
    try:
        task = self.task_list.get_task(ix)
        task.mark_completed()
    except IndexError:
        print("Task does not exist. Please try again.")

# Controller (Exercise 7)
class TaskManagerController:
    def __init__(self, task_list):
        self.task_list = task_list

    def add_task(self, title, date):
        task = TaskFactory.create_task(title, date)
        self.task_list.add_task(task)

    def complete_task(self, ix):
        if self.task_list.check_task_index(ix):
            self.task_list.get_task(ix).mark_completed()

# UI (Exercise 7)
class CommandLineUI:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        while True:
            self._print_menu()
            choice = input("Enter choice: ")
            if choice == '1':
                title = input("Enter task title: ")
                date_str = input("Enter task date (YYYY-MM-DD): ")
                date = datetime.strptime(date_str, "%Y-%m-%d")
                self.controller.add_task(title, date)
            elif choice == '2':
                ix = int(input("Enter task index to complete: "))
                self.controller.complete_task(ix)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")

# Factory Usage
task = TaskFactory.create_task(
    "Go to gym",
    datetime.now(),
    interval=timedelta(days=7)
)