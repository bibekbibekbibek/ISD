# SRP: Handles input/output ONLY (no business logic)
class CommandLineUI:
    def __init__(self, controller):
        # Separation of concerns: UI depends on controller
        self.controller = controller

    def run(self):
        while True:
            self.print_menu()
            choice = input("Choose option: ")

            if choice == "1":
                self.add_task_ui()
            elif choice == "2":
                self.add_recurring_task_ui()
            elif choice == "3":
                self.complete_task_ui()
            elif choice == "4":
                self.delete_task_ui()
            elif choice == "5":
                self.show_tasks()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid option!")

    def print_menu(self):
        print("\n--- ToDo App ---")
        print("1. Add Task")
        print("2. Add Recurring Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Show Tasks")
        print("0. Exit")

    def add_task_ui(self):
        title = input("Enter title: ")
        try:
            # Exception Handling: catches invalid input
            days = int(input("Days from today until due: "))
            self.controller.add_task(title, days)
        except ValueError:
            print("Invalid number!")

    def add_recurring_task_ui(self):
        title = input("Enter title: ")
        try:
            days = int(input("Days from today until first due date: "))
            interval = int(input("How often to repeat (in days): "))
            self.controller.add_recurring_task(title, days, interval)
        except ValueError:
            print("Invalid input!")

    def complete_task_ui(self):
        try:
            index = int(input("Enter task index: "))
            
            # Controller handles logic, UI shows result
            if not self.controller.complete_task(index):
                print("Invalid index!")
        except ValueError:
            print("Enter a number!")

    def delete_task_ui(self):
        try:
            index = int(input("Enter task index: "))
            if not self.controller.delete_task(index):
                print("Invalid index!")
        except ValueError:
            print("Enter a number!")

    def show_tasks(self):
        tasks = self.controller.get_all_tasks()
        if not tasks:
            print("No tasks available.")
            return

        for i, task in enumerate(tasks):
            print(f"{i}: {task}")