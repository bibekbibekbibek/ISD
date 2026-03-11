# # Exercise 1 Task 1: Creating Classes and Initializing Objects

# class TaskList:
#     def __init__(self, subject):
#         self.subject = subject
#         # self.subject = subject.upper()
#         self.tasks = []

# my_tasks_list = TaskList("Python Programming")
# print(my_tasks_list.subject)

# # Exercise 1 Task 2: Adding, Deleting, Viewing Methods to a Class

# class TaskList:
#     def __init__(self, subject):
#         self.subject = subject
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def delete_task(self, task):
#         self.tasks.remove(task)

#     def view_tasks(self):
#         return self.tasks

# my_tasks_list = TaskList("Python Programming")
# my_tasks_list.add_task("Complete lab exercises, submit assignment")
# print("before deletion:", my_tasks_list.view_tasks())
# my_tasks_list.delete_task("Complete lab exercises, submit assignment")
# print("after deletion:", my_tasks_list.view_tasks())

# # Task: Add the code to the remove_task method. Hint: You can use the del keyword to remove an item
# # from a list. For example, if you wanted to remove the item at index 0 from a list called my_list, you
# # could do this as follows: del my_list[0].

# class TaskList:
#     def __init__(self, subject):
#         self.subject = subject
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def remove_task(self, index):
#         if 0 <= index < len(self.tasks):
#             del self.tasks[index]
#             # print("Task removed successfully!")
#         else:
#             print("Invalid index!")

#     def view_tasks(self):
#         return self.tasks
    

# my_tasks_list = TaskList("Python Programming")
# my_tasks_list.add_task("Complete lab exercises")
# my_tasks_list.add_task("Submit assignment")
# print("before deletion:", my_tasks_list.view_tasks())
# my_tasks_list.remove_task(0)
# print("after deletion:", my_tasks_list.view_tasks())


# # Task: Add the code to the view_tasks method. Rather than printing the tasks list directly, you should
# # iterate over the tasks list and print each task individually and also include its index. Hint: You can use a
# # for loop to iterate over the tasks list. (Hint 2: If you want to be very efficient, read up on the enumerate
# # function in Python https://sparkbyexamples.com/python/for-loop-enumerate-in-python/ ) 

# class TaskList:
#     def __init__(self, subject):
#         self.subject = subject
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)
#         print("Task added successfully!")

#     def remove_task(self, index):
#         if 0 <= index < len(self.tasks):
#             del self.tasks[index]
#             print("Task removed successfully!")
#         else:
#             print("Invalid index!")

#     def view_tasks(self):
#         if not self.tasks:
#             print("No tasks to display.")
#         else:
#             print("Tasks:")
#             for index, task in enumerate(self.tasks):
#                 print(f"{index}: {task}")

#     def list_options(self):
#         while True:
#             print("\nTo-Do List Manager")
#             print("1. Add a task")
#             print("2. View tasks")
#             print("3. Remove a task")
#             print("4. Quit")
#             choice = input("Enter your choice: ")
#             if choice == "1":
#                 task = input("Enter a task: ")
#                 self.add_task(task)
#             elif choice == "2":
#                 self.view_tasks()
#             elif choice == "3":
#                 try:
#                     index = int(input("Enter the index of the task to remove: "))
#                     self.remove_task(index)
#                 except ValueError:
#                     print("Please enter a valid integer for the index.")
#             elif choice == "4":
#                 print("Exiting To-Do List Manager. Goodbye!")
#                 break
#             else:
#                 print("Invalid choice! Please enter a number between 1 and 4.")

# my_tasks_list = TaskList("Python Programming")
# my_tasks_list.list_options()

# # Exercise 1 Task 3: Testing the Functionality
# class TaskList:
#     def __init__(self, subject):
#         self.subject = subject
#         self.tasks = []

#     def add_task(self, *tasks):
#         for task in tasks:
#             self.tasks.append(task)
#         print("Tasks added successfully!")

#     def remove_task(self, index):
#         if 0 <= index < len(self.tasks):
#             del self.tasks[index]
#             print("Task removed successfully!")
#         else:
#             print("Invalid index!")

#     def view_tasks(self):
#         if not self.tasks:
#             print("No tasks to display.")
#         else:
#             print("Tasks:")
#             for index, task in enumerate(self.tasks):
#                 print(f"{index}: {task}")

# my_tasks_list = TaskList("Your Name")
# my_tasks_list.add_task("Do Homework", "Submit Assignment", "Study for Exam")
# print("Tasks after adding:", my_tasks_list.view_tasks())
# my_tasks_list.remove_task(1)
# print("Tasks after removing index 1:", my_tasks_list.view_tasks())

# # Exercise 1 Task 4: Composition
# class Task:
#     def __init__(self, title):
#         self.title = title

#     def __str__(self):
#         return f"Task: {self.title}"

# class TaskList:
#     def __init__(self, subject):
#         self.subject = subject
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)
#         print("Task added successfully!")

#     def remove_task(self, index):
#         if 0 <= index < len(self.tasks):
#             del self.tasks[index]
#             print("Task removed successfully!")
#         else:
#             print("Invalid index!")

#     def view_tasks(self):
#         if not self.tasks:
#             print("No tasks available.")
#             return
        
#         print("\nYour Tasks:")
#         for index, task in enumerate(self.tasks):
#             print(f"{index}: {task}")

#     def list_options(self):
#         while True:
#             print("\nTo-Do List Manager")
#             print("1. Add a task")
#             print("2. View tasks")
#             print("3. Remove a task")
#             print("4. Quit")

#             choice = input("Enter your choice: ")

#             if choice == "1":
#                 title = input("Enter a task: ")
#                 task = Task(title)
#                 self.add_task(task)

#             elif choice == "2":
#                 self.view_tasks()

#             elif choice == "3":
#                 try:
#                     ix = int(input("Enter the index of the task to remove: "))
#                     self.remove_task(ix)
#                 except ValueError:
#                     print("Please enter a valid number!")

#             elif choice == "4":
#                 print("Goodbye!")
#                 break

#             else:
#                 print("Invalid choice! Please select 1-4.")

# my_task_list = TaskList("Python Programming")

# my_task_list.tasks = [
#     Task("Do Homework"),
#     Task("Do Laundry"),
#     Task("Go Shopping")
# ]

# my_task_list.list_options()

# # Exerxise 1 Task 5: Developing Task

# class TaskList:
#     def __init__(self, subject):
#         self.subject = subject
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)
#         print("Task added successfully!")

#     def remove_task(self, index):
#         if 0 <= index < len(self.tasks):
#             del self.tasks[index]
#             print("Task removed successfully!")
#         else:
#             print("Invalid index!")

#     def view_tasks(self):
#         if not self.tasks:
#             print("No tasks to display.")
#         else:
#             print("Tasks:")
#             for index, task in enumerate(self.tasks):
#                 print(f"{index}: {task}")
    
#     def Mark_task_completed(self, index):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index] += " (Completed)"
#             print("Task marked as completed!")
#         else:
#             print("Invalid index!")
    
#     def change_task_title(self, index, new_title):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index] = new_title
#             print("Task title changed successfully!")
#         else:
#             print("Invalid index!")

#     def list_options(self):
#         while True:
#             print("\nTo-Do List Manager")
#             print("1. Add a task")
#             print("2. View tasks")
#             print("3. Remove a task")
#             print("4. Mark a task as completed")
#             print("5. Change Task Title")
#             print("6. Quit")
#             choice = input("Enter your choice: ")
#             if choice == "1":
#                 task = input("Enter a task: ")
#                 self.add_task(task)
#             elif choice == "2":
#                 self.view_tasks()
#             elif choice == "3":
#                 try:
#                     index = int(input("Enter the index of the task to remove: "))
#                     self.remove_task(index)
#                 except ValueError:
#                     print("Please enter a valid integer for the index.")
            
#             elif choice == "4":
#                 try:
#                     index = int(input("Enter the index of the task to mark as completed: "))
#                     self.Mark_task_completed(index)
#                 except ValueError:
#                     print("Please enter a valid integer for the index.")

#             elif choice == "5":
#                 try:
#                     index = int(input("Enter the index of the task to change: "))
#                     new_title = input("Enter the new title for the task: ")
#                     self.change_task_title(index, new_title)
#                 except ValueError:
#                     print("Please enter a valid integer for the index.")

#             elif choice == "6":
#                 print("Exiting To-Do List Manager. Goodbye!")
#                 break
#             else:
#                 print("Invalid choice! Please enter a number between 1 and 6.")

# my_tasks_list = TaskList("Python Programming")
# my_tasks_list.list_options()


# # Exercise 2 Task 1: Adding Dates

# import datetime

# # date = datetime.datetime(2026, 5, 3)
# # print(date)
# # date = datetime.datetime.strptime("2026-05-03 1:00:00", "%Y-%m-%d %H:%M:%S")
# # print(date)

# class Task:
#     def __init__(self, title, date_due):
#         self.title = title
#         self.date_created = datetime.datetime.now()
#         self.date_due = date_due

# task = Task("Complete lab exercises", datetime.datetime.strptime("2026-05-03 1:00:00", "%Y-%m-%d %H:%M:%S"))
# print("Task Title:", task.title)
# print("Date Created:", task.date_created)
# print("Date Due:", task.date_due)

# # Task: In the same format as above, add the option to change the due date of a task. It is most likely that
# # in your user options, you will need to add an additional option for editing a task, where you can group
# # the option to change the title and the due date. 

# import datetime

# class Task:
#     def __init__(self, title, date_due):
#         self.title = title
#         self.date_created = datetime.datetime.now()
#         self.date_due = date_due

#     def change_title(self, new_title):
#         self.title = new_title

#     def change_due_date(self, new_due_date):
#         self.date_due = new_due_date

#     def display(self):
#         print("Title:", self.title)
#         print("Created:", self.date_created)
#         print("Due Date:", self.date_due)


# class TaskList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, title, date_due):
#         task = Task(title, date_due)
#         self.tasks.append(task)

#     def view_tasks(self):
#         if len(self.tasks) == 0:
#             print("No tasks available.")
#         else:
#             for i, task in enumerate(self.tasks):
#                 print("\nTask", i + 1)
#                 task.display()

#     def delete_task(self, index):
#         if 0 <= index < len(self.tasks):
#             del self.tasks[index]
#             print("Task deleted.")
#         else:
#             print("Invalid task number.")

#     def edit_task(self, index):
#         if 0 <= index < len(self.tasks):
#             task = self.tasks[index]

#             print("\n1. Change Title")
#             print("2. Change Due Date")

#             choice = input("Choose option: ")

#             if choice == "1":
#                 new_title = input("Enter new title: ")
#                 task.change_title(new_title)

#             elif choice == "2":
#                 new_due_date = input("Enter new due date: ")
#                 task.change_due_date(new_due_date)

#             else:
#                 print("Invalid choice.")
#         else:
#             print("Invalid task number.")


# task_list = TaskList()

# while True:
#     print("\n----- Task Manager -----")
#     print("1. Add Task")
#     print("2. View Tasks")
#     print("3. Edit Task")
#     print("4. Delete Task")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         title = input("Enter task title: ")
#         due_date = input("Enter due date: ")
#         task_list.add_task(title, due_date)

#     elif choice == "2":
#         task_list.view_tasks()

#     elif choice == "3":
#         task_list.view_tasks()
#         num = int(input("Enter task number to edit: ")) - 1
#         task_list.edit_task(num)

#     elif choice == "4":
#         task_list.view_tasks()
#         num = int(input("Enter task number to delete: ")) - 1
#         task_list.delete_task(num)

#     elif choice == "5":
#         print("Exiting program.")
#         break

#     else:
#         print("Invalid choice.")


    
