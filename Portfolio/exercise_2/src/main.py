from tasks import Task
from tasklist import TaskList

def main():
    task_list = TaskList("John Doe")

    while True:
        task_list.list_options()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            description = input("Enter task description (optional): ")
            task = Task(title, due_date, description)
            task_list.add_task(task)

        elif choice == "2":
            index = int(input("Enter task index to remove: ")) - 1
            task_list.remove_task(index)

        elif choice == "3":
            task_list.view_tasks()

        elif choice == "4":
            index = int(input("Enter task index to edit: ")) - 1
            new_title = input("Enter new title (leave blank to keep current): ")
            new_due_date = input("Enter new due date (YYYY-MM-DD, leave blank to keep current): ")
            new_description = input("Enter new description (leave blank to keep current): ")
            task_list.edit_task(index, new_title or None, new_due_date or None, new_description or None)

        elif choice == "5":
            task_list.view_overdue_tasks()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()