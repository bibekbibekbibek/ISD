import datetime
from tasks import Task, RecurringTask
from tasklist import TaskList


def main():
    owner = input("Enter owner name: ")
    task_list = TaskList(owner)

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Completed")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            date = input("Due date (YYYY-MM-DD): ")
            due_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

            recurring = input("Recurring? (y/n): ")

            if recurring.lower() == "y":
                days = int(input("Interval (days): "))
                interval = datetime.timedelta(days=days)
                task = RecurringTask(title, desc, due_date, interval)
            else:
                task = Task(title, desc, due_date)

            task_list.add_task(task)

        elif choice == "2":
            task_list.view_tasks()

        elif choice == "3":
            ix = int(input("Index: "))
            task_list.remove_task(ix)

        elif choice == "4":
            ix = int(input("Index: "))
            task = task_list.get_task(ix)
            if task:
                task.mark_completed()
                print("Task updated")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()