# SRP: Handles input/output ONLY (no business logic)
class CommandLineUI:
    def __init__(self, controller):
        # Separation of concerns: UI depends on controller
        self.controller = controller

    def run(self) -> None:
        """Run the main application loop."""
        self.print_welcome()
        
        while True:
            self.print_menu()
            choice = input("Choose option: ").strip()

            if choice == "1":
                self.add_task_ui()
            elif choice == "2":
                self.add_recurring_task_ui()
            elif choice == "3":
                self.add_priority_task_ui()
            elif choice == "4":
                self.complete_task_ui()
            elif choice == "5":
                self.delete_task_ui()
            elif choice == "6":
                self.show_tasks()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid option!")

    def print_welcome(self) -> None:
        """Print welcome message with instructions."""
        print("\n" + "="*60)
        print("Welcome to ToDo App!")
        print("="*60)
        print("\n   HOW TO ENTER DATES:")
        print("   When asked 'Days from today until due', enter a NUMBER:")
        print("   • 0  = Today")
        print("   • 1  = Tomorrow")
        print("   • 7  = Next week")
        print("   • 30 = About a month from now")
        print("   • 365= About a year from now")
        print("\n   Example: If today is April 4, and you enter '7'")
        print("   the task will be due on April 11 (7 days later)")
        print("="*60 + "\n")

    def print_menu(self) -> None:
        """Print the main menu."""
        print("\n--- ToDo App Menu ---")
        print("1. Add Task (enter days from today)")
        print("2. Add Recurring Task (repeating at intervals)")
        print("3. Add Priority Task (Low/Medium/High)")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Show All Tasks")
        print("0. Exit")

    def add_task_ui(self) -> None:
        """UI for adding a regular task."""
        title = input("Enter title: ").strip()
        if not title:
            print("Task title cannot be empty!")
            return
        
        try:
            # Exception Handling: catches invalid input
            days = int(input("Days from today until due (e.g., 1 for tomorrow, 7 for next week): "))
            if self.controller.add_task(title, days):
                print("✓ Task added successfully!")
            else:
                print("✗ Failed to add task")
        except ValueError:
            print("Please enter a valid number (e.g., 1, 7, 30)")

    def add_recurring_task_ui(self) -> None:
        """UI for adding a recurring task."""
        title = input("Enter title: ").strip()
        if not title:
            print("Task title cannot be empty!")
            return
        
        try:
            days = int(input("Days from today until first due date (e.g., 0 for today, 1 for tomorrow): "))
            interval = int(input("How often to repeat in days (e.g., 7 for weekly, 14 for bi-weekly): "))
            if self.controller.add_recurring_task(title, days, interval):
                print("✓ Recurring task added successfully!")
            else:
                print("✗ Failed to add recurring task")
        except ValueError:
            print("Please enter valid numbers!")

    def add_priority_task_ui(self) -> None:
        """UI for adding a priority task."""
        title = input("Enter title: ").strip()
        if not title:
            print("Task title cannot be empty!")
            return
        
        try:
            days = int(input("Days from today until due (e.g., 1 for tomorrow, 7 for next week): "))
            
            print("\nPriority levels:")
            print("  1 - Low    (e.g., Nice to have, someday)")
            print("  2 - Medium (e.g., Important, should do)")
            print("  3 - High   (e.g., Urgent, must do)")
            priority = int(input("Enter priority (1, 2, or 3): "))
            
            if self.controller.add_priority_task(title, days, priority):
                print("✓ Priority task added successfully!")
            else:
                print("✗ Failed to add priority task")
        except ValueError as e:
            print(f"Please enter valid numbers! {e}")

    def complete_task_ui(self) -> None:
        """UI for marking a task as completed."""
        try:
            index = int(input("Enter task index: "))
            
            # Controller handles logic, UI shows result
            if self.controller.complete_task(index):
                print("✓ Task completed!")
            else:
                print("✗ Invalid index!")
        except ValueError:
            print("Enter a number!")

    def delete_task_ui(self) -> None:
        """UI for deleting a task."""
        try:
            index = int(input("Enter task index: "))
            if self.controller.delete_task(index):
                print("✓ Task deleted!")
            else:
                print("✗ Invalid index!")
        except ValueError:
            print("Enter a number!")

    def show_tasks(self) -> None:
        """Display all tasks."""
        tasks = self.controller.get_all_tasks()
        if not tasks:
            print("No tasks available.")
            return

        print("\n--- Tasks ---")
        for i, task in enumerate(tasks):
            print(f"{i}: {task}")
