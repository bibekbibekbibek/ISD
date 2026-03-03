# In this exercise, you will create a simple to-do list program using Python. You will use variables, lists, input,
# loops, functions, and conditionals to build a basic but functional to-do list manager.
# Task: To-Do list manager
# You need to create a to-do list manager with the following functionalities:
# 1. Initialize an empty list to store tasks.
# 2. Implement a menu that allows the user to perform the following actions:
# • Add a new task to the list.
# • View the current tasks in the list.
# • Remove a task from the list.
# • Quit and exit the program.
# 3. Use a while loop to repeatedly display the menu and handle user input.
# 4. Create functions for adding, viewing, and removing tasks.
# 5. Use conditionals to execute the appropriate function based on the user's choice.
# 6. Display a message if the user tries to remove a task that doesn't exist.
# 7. Exit the program when the user chooses to quit.

tasks = []

def add_task():
    tasks.append(input("Enter a new task: "))
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("Current tasks:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")   

def remove_task():
    if len(tasks) == 0:
        print("No tasks to remove.")
    else:
        view_tasks()
        try:
            task_number = int(input("Enter the number of the task to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

while True:
    print("\nTo-Do List Manager")
    print("1. Add a new task")
    print("2. View current tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.") 

