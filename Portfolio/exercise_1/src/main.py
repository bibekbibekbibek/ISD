from  tasks import Task
from tasklist import TaskList

def main():
    task_list = TaskList()

    while True: 
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Edit Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            due_date = input("Enter task due date: ")
            description = input("Enter task description (optional): ")
            task = Task(title, due_date, description)
            task_list.add_task(task)
            print("Task added successfully.\n")

        elif choice == '2':
            index = int(input("Enter the task number to remove: ")) - 1
            task_list.remove_task(index)

        elif choice == '3':
            task_list.show_tasks()

        elif choice == '4':
            task_list.show_tasks()
            index = int(input("Enter the task number to edit: ")) - 1
            if 0 <= index < len(task_list.tasks):
                new_title = input("Enter new title (leave blank to keep current): ")
                new_due_date = input("Enter new due date (leave blank to keep current): ")
                new_description = input("Enter new description (leave blank to keep current): ")

                task_list.tasks[index].change_title(new_title)
                task_list.tasks[index].change_due_date(new_due_date)
                task_list.tasks[index].change_description(new_description)   
                print("Task updated successfully.\n")
            else:
                print("Invalid task number.\n")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":    
    main()

        