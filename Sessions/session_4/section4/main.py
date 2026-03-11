from tasks import Task
from tasklist import TaskList


def main() -> None:
    task_list: TaskList = TaskList()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Exit")

        choice: str = input("Enter choice: ")

        if choice == "1":
            title: str = input("Enter task title: ")
            description: str = input("Enter task description: ")

            task: Task = Task(title, description)
            task_list.add_task(task)

        elif choice == "2":
            task_list.display_tasks()

        elif choice == "3":
            index: int = int(input("Enter task number to complete: "))
            task: Task | None = task_list.get_task(index)

            if task:
                task.mark_complete()
            else:
                print("Task not found")

        elif choice == "4":
            index: int = int(input("Enter task number to remove: "))
            task_list.remove_task(index)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()