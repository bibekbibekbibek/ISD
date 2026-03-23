import datetime
from tasks import Task, RecurringTask
from tasklist import TaskList


def main():

    owner = input("Enter task list owner: ")
    task_list = TaskList(owner)

    while True:

        task_list.list_options()
        choice = input("Enter choice: ")

        if choice == "1":

            title = input("Enter task title: ")
            description = input("Enter description: ")

            date_input = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()

            recurring = input("Is this a recurring task? (y/n): ")

            if recurring.lower() == "y":

                interval = input("Enter interval in days: ")
                interval = datetime.timedelta(days=int(interval))

                task = RecurringTask(title, description, due_date, interval)

            else:
                task = Task(title, description, due_date)

            task_list.add_task(task)

        elif choice == "2":

            task_list.view_tasks()

        elif choice == "3":

            ix = int(input("Enter task number to remove: "))
            task_list.remove_task(ix)

        elif choice == "4":

            task_list.view_overdue_tasks()

        elif choice == "5":

            ix = int(input("Enter task number to mark completed: "))
            task = task_list.get_task(ix)

            if task:
                task.mark_completed()
                print("Task marked as completed")

        elif choice == "6":

            print("Goodbye")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()



from tasklist import TaskList

def main():
    task_list = TaskList()

    while True:
        print("\nToDo List Menu")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Mark Task as Completed")
        print("5. View Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            task_list.add_task(description)

        elif choice == "2":
            index = int(input("Enter task index to remove: "))
            task_list.remove_task(index)

        elif choice == "3":
            task_list.list_tasks()

        elif choice == "4":
            index = int(input("Enter task index to mark as completed: "))
            task = task_list.get_task(index)

            if task:
                task.completed = True
                print("Task marked as completed.")

        elif choice == "5":
            index = int(input("Enter task index to view: "))
            task = task_list.get_task(index)

            if task:
                status = "Completed" if task.completed else "Pending"
                print(f"Task: {task.description} - {status}")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()