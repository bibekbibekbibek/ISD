from tasklist import TaskList
from tasks import Task, RecurringTask
from users import Owner
import datetime


def propagate_task_list(task_list: TaskList) -> TaskList:
    task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)))
    task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)))

    r_task = RecurringTask("Go to gym", datetime.datetime.now(), datetime.timedelta(days=7))
    task_list.add_task(r_task)

    return task_list


def main() -> None:
    # ✅ Create Owner object
    name = input("Enter owner name: ")
    email = input("Enter owner email: ")

    owner = Owner(name, email)

    # ✅ Pass Owner object instead of string
    task_list = TaskList(owner)

    task_list = propagate_task_list(task_list)

    while True:
        print("\nTo-Do List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Edit a task")
        print("5. Complete a task")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter a task: ")
            input_date = input("Enter due date (YYYY-MM-DD): ")
            date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")

            recurring = input("Is this recurring? (y/n): ")

            if recurring == "y":
                interval = int(input("Interval in days: "))
                task = RecurringTask(title, date_object, datetime.timedelta(days=interval))
            else:
                task = Task(title, date_object)

            task_list.add_task(task)

        elif choice == "2":
            task_list.view_tasks()

        elif choice == "3":
            ix = int(input("Index to remove: "))
            task_list.remove_task(ix)

        elif choice == "4":
            ix = int(input("Index to edit: "))
            field = input("Edit title or due date? ")

            if field == "title":
                new_title = input("New title: ")
                task_list.get_task(ix).change_title(new_title)

            elif field == "due date":
                new_date = input("New date (YYYY-MM-DD): ")
                date_object = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                task_list.get_task(ix).change_date_due(date_object)

        elif choice == "5":
            ix = int(input("Index to complete: "))
            task_list.get_task(ix).mark_completed()

        elif choice == "6":
            break


if __name__ == "__main__":
    main()