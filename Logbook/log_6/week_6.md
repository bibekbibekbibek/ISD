# Session 6 : Debugging, Properties and Persistence

## Section 1 Debugging

### Exercise 1 Task 1 : Finding the Problem

```Python
class Car:

    def __init__(self, speed:str=0) -> None:
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def accelerate(self) -> None:
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self)  -> None:
        self.odometer += self.speed
        self.time += 1

    def average_speed(self) -> float:
        return self.odometer / self.time


if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                        "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
            print("Accelerating...")
        elif action == 'B':
            my_car.brake()
            print("Braking...")
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()
```

Output
The program was first run by accelerating once and braking twice, then displaying the odometer. The output showed 0 km, which is incorrect.

To find the issue, a breakpoint was set at:

self.odometer += self.speed

Using the debugger, the variable values were observed:

After acceleration: speed = 5
After braking twice: speed = -5

The speed becoming negative caused the odometer value to decrease, resulting in an incorrect distance.
``` Console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_6/lab_week_6_debugging.py
I'm a car!
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?A
Accelerating...
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?B
Braking...
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?B
Braking...
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?O
The car has driven 0 kilometers
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?S
The car's average speed was -1.25 kph
```

### Exercise 1 Task 2 : Fixing the Problem

``` python
class Car:

    def __init__(self, speed:str=0) -> None:
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def accelerate(self) -> None:
        self.speed += 5

    # def brake(self):
    #     self.speed -= 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def step(self)  -> None:
        self.odometer += self.speed
        self.time += 1

    def average_speed(self) -> float:
        return self.odometer / self.time


if __name__ == '__main__':

    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                        "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
            print("Accelerating...")
        elif action == 'B':
            my_car.brake()
            print("Braking...")
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()
```

Output
To fix the issue, the brake() method was modified to prevent the speed from becoming negative.

Corrected Code
def brake(self):
    if self.speed >= 5:
        self.speed -= 5
    else:
        self.speed = 0

After applying this fix, the program was run again by accelerating once and braking twice. The odometer then correctly showed 5 km.
``` Console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_6/lab_week_6_debugging.py
I'm a car!
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?A
Accelerating...
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?B
Braking...
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?B
Braking...
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?O
The car has driven 5 kilometers
What should I do? [A]ccelerate, [B]rake, show [O]dometer, or show average [S]peed?S
The car's average speed was 1.25 kph
```

### Exercise 1 Task 3 : Stepping Through the Code

In this exercise, the debugger was used to step through the code line by line. After starting the debugger and accelerating the car, the Step Over function was used to move through each line of the program.

The Step Into function was also used to enter the accelerate() method, allowing observation of how the speed value increases. This helped in understanding how the function works internally.

### Exercise 1 Task 4 : Watching Variables or Expressions 

In this exercise, the Watch feature in the debugger was used to monitor specific variables during program execution. The variable my_car.speed was added to the Watch section.

This allowed the value of the speed to be observed continuously without needing to expand the Variables panel. An expression such as my_car.speed > 0 was also added to check conditions during execution.

## Section 2 Properties using the @property decorator
Task: Modify the view_tasks method of the TaskList class to only show the uncompleted tasks using
the new property. Change the text that is printed to something along the lines of "The following tasks are
still to be done:" so that users know that they are looking at the uncompleted tasks. Ensure that you show
the right indices by removing the “enumerate” statement and using the index() method to get the index
for printing out the task info in the format: print(f"{ix}: {task}"). This is important as you are
now using the uncompleted_tasks property and are hiding the completed tasks. 

``` Python
#tasks.py
import datetime

class Task:
    def __init__(self, title: str, description: str, due_date: datetime.date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.title} | Due: {self.due_date} | {status}"


class RecurringTask(Task):
    def __init__(self, title, description, due_date, interval):
        super().__init__(title, description, due_date)
        self.interval = interval

    def mark_completed(self):
        # Move to next due date instead of finishing
        self.due_date += self.interval

    def __str__(self):
        return f"{self.title} (Recurring) | Due: {self.due_date}"
```

``` Python
#tasklist.py
from tasks import Task

class TaskList:
    def __init__(self, owner: str):
        self.owner = owner
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, ix: int):
        if 0 <= ix < len(self.tasks):
            self.tasks.pop(ix)
        else:
            print("Task not found")

    def get_task(self, ix: int):
        if 0 <= ix < len(self.tasks):
            return self.tasks[ix]
        return None

    @property
    def uncompleted_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def view_tasks(self):
        print("The following tasks are still to be done:")

        if not self.uncompleted_tasks:
            print("No remaining tasks")
            return

        for task in self.uncompleted_tasks:
            ix = self.tasks.index(task)
            print(f"{ix}: {task}")
```

``` Python
# main.py
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
```

Output
``` Console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_6/ToDo/main.py
Enter owner name: Bibek

1. Add Task      
2. View Tasks    
3. Remove Task   
4. Mark Completed
5. Exit
Choose: 1
Title: Java
Description: Qwerty
Due date (YYYY-MM-DD): 2026-3-30
Recurring? (y/n): 3

1. Add Task
2. View Tasks
3. Remove Task
4. Mark Completed
5. Exit
Choose: 2
The following tasks are still to be done:
0: Java | Due: 2026-03-30 | ✗

1. Add Task
2. View Tasks
3. Remove Task
4. Mark Completed
5. Exit
Choose: 4
Index: 0
Task updated

1. Add Task
2. View Tasks
3. Remove Task
4. Mark Completed
5. Exit
Choose: 2
The following tasks are still to be done:
No remaining tasks

1. Add Task
2. View Tasks
3. Remove Task
4. Mark Completed
5. Exit
Choose: 5
Goodbye!
```

## Section 3 Implementing Persistence 

Persistence is implemented using the DAO pattern and a CSV file to save and load tasks.
In Task A, tasks are read from the CSV file using get_all_tasks() and added to the task list:

tasks = dao.get_all_tasks()

Dates are converted using strptime, and empty values are ignored to avoid errors.
In Task B, tasks are saved using save_all_tasks() by converting data to strings:

row["date_due"] = task.date_due.strftime("%Y-%m-%d")

This allows the application to store and retrieve tasks between sessions.

``` python
# main.py
from tasklist import TaskList
from tasks import Task, RecurringTask
from dao import TaskTestDAO, TaskCsvDAO
import datetime


def main() -> None:
    task_list = TaskList("YOUR NAME")



    while True: 
        print("To-Do List Manager") 
        print("1. Add a task") 
        print("2. View tasks") 
        print("3. Remove a task")
        print("4. Edit a task")
        print("5. Complete a task")
        print("6. Import tasks")
        print("7. Export tasks")
        print("q. Quit")
            
        choice = input("Enter your choice: ") 
            
        if choice == "1":
            title = input("Enter a task: ")
            input_date = input("Enter a due date (YYYY-MM-DD): ")
            date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")

            reccuring = input("Is this a reccuring task? (y/n): ")
            if reccuring == "y":
                interval = int(input("Enter the interval between each repetition (days): "))
                recurring_task = RecurringTask(title, date_object, interval=datetime.timedelta(days=int(interval)))
                task_list.add_task(recurring_task)
            else:
                # create a new task object based on the title entered and the date entered
                task = Task(title, date_object)
                task_list.add_task(task)

        elif choice == "2":
            task_list.view_tasks()

        elif choice == "3":
            ix = int(input("Enter the index of the task to remove: "))
            try:
                task_list.get_task(ix)
            except IndexError:
                print("Invalid index.")
                continue
            
            task_list.remove_task(ix)
    
        elif choice == "4":
            ix = int(input("Enter the index of the task to edit: "))
            choice = input("What would you like to edit? (title/due date): ")
            

            try:
                task = task_list.get_task(ix)
            except IndexError:
                print("Invalid index.")
                continue

            if choice == "title":
                title = input("Enter a new title: ")
                task.change_title(title)
            elif choice == "due date":
                input_date = input("Enter a new due date (YYYY-MM-DD): ")
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task.change_date_due(date_object)
            else:
                print("Invalid choice.")
        
        elif choice == "5":
            ix = int(input("Enter the index of the task to complete: "))

            try:
                task = task_list.get_task(ix)
            except IndexError:
                print("Invalid index.")
                continue

            task.mark_completed()

        elif choice == "6":
            task_path = input("Enter the path to the task file: ")
            dao = TaskCsvDAO(task_path)
            tasks = dao.get_all_tasks()
            for task in tasks:
                task_list.add_task(task)
        elif choice == "7":
            task_path = input("Enter the path to save the task file: ")
            dao = TaskCsvDAO(task_path)
            dao.save_all_tasks(task_list.tasks)

        elif choice == "q":
            break



if __name__ == "__main__":
    main()
```

``` python
# dao.py
from tasks import Task, RecurringTask
import datetime

class TaskTestDAO:
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path

    def get_all_tasks(self) -> list[Task]:
        task_list =[
            Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)),
            Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2)),
            Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1)),
            Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)),
            Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)),
            Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6))
        ]

        # sample recurring task
        r_task = RecurringTask("Go to the gym", datetime.datetime.now(), datetime.timedelta(days=7))
        # propagate the recurring task with some completed dates
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=7))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=14))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=22))
        r_task.date_created = datetime.datetime.now() - datetime.timedelta(days=28)

        task_list.append(r_task)

        return task_list

    def save_all_tasks(self, tasks: list[Task]) -> None:
        pass


import csv
class TaskCsvDAO:
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path

        self.fieldnames = ["title", "type", "date_due", "completed", "interval", "completed_dates", "date_created"]

    def get_all_tasks(self) -> list[Task]:
        task_list : list[Task]= []
        with open(self.storage_path, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                task_type = row["type"]
                task_title = row["title"]
                task_date_due = row["date_due"]
                task_completed = row["completed"]
                task_interval = row["interval"]
                task_date_created = row["date_created"]
                task_completed_dates = row["completed_dates"]

                # YOUR CODE TASK A
                task: Task | RecurringTask # declare the type of task as Task or RecurringTask for the type checker
                
                if task_type == "RecurringTask":
                    interval_days = int(task_interval.split(" ")[0])
                    task = RecurringTask(task_title, datetime.datetime.strptime(task_date_due, "%d/%m/%Y"), datetime.timedelta(days=interval_days))
                    task.completed_dates = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in task_completed_dates.split(",") if date]
                    task.date_created = datetime.datetime.strptime(task_date_created, "%d/%m/%Y")
                else:
                    task = Task(task_title, datetime.datetime.strptime(task_date_due, "%d/%m/%Y"))
                    task.date_created = datetime.datetime.strptime(task_date_created, "%d/%m/%Y")
                
                task.completed = True if task_completed.lower() == "true" else False
                
                task_list.append(task)
        return task_list



    def save_all_tasks(self, tasks: list[Task]) -> None:
        with open(self.storage_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for task in tasks:
                row = {}


                # YOUR CODE FOR TASK B BELOW

                row["title"] = task.title
                row["type"] = "RecurringTask" if isinstance(task, RecurringTask) else "Task"
                row["date_due"] = task.date_due.strftime("%d/%m/%Y")
                row["completed"] = str(task.completed)
                row["interval"]  = str(task.interval) if isinstance(task, RecurringTask) else ""
                row["completed_dates"] = ",".join([date.strftime("%Y-%m-%d") for date in task.completed_dates]) if isinstance(task, RecurringTask) else ""
                row["date_created"] = task.date_created.strftime("%d/%m/%Y")
                writer.writerow(row)
```

``` python
# tasks.py
import datetime

class Task:
    """Represents a task in a to-do list. <-- this is a class docstring.
    """

    def __init__(self, title: str, date_due: datetime.datetime):
        """Creates a new task. <-- this is a method docstring.

        Args:
            title (str): Title of the task.
            date_due (datetime.datetime): Due date of the task.
        """
        self.title = title
        self.date_created = datetime.datetime.now()
        self.completed = False
        self.date_due = date_due

    def change_title(self, new_title: str) -> None:
        """Changes the title of the task.

        Args:
            new_title (str): New title of the task.
        """
        self.title = new_title

    def change_date_due(self, date_due: datetime.datetime) -> None:
        """Changes the due date of the task.

        Args:
            date_due (datetime.datetime): New due date of the task.
        """
        self.date_due = date_due

    def mark_completed(self) -> None:
        """Marks the task as completed."""

        self.completed = True

    def __str__(self) -> str:
        return f"{self.title} (created: {self.date_created}, due: {self.date_due}, completed: {self.completed})"
    


class RecurringTask(Task):
    """Represents a recurring task in a to-do list.

    Args:
        Task (Task): The task to be repeated.
    """

    def __init__(self, title: str, date_due: datetime.datetime, interval: datetime.timedelta):
        """Creates a new recurring task.

        Args:
            title (str): Title of the task.
            date_due (datetime.datetime): Due date of the task.
            interval (datetime.timedelta): Interval between each repetition.
        """
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates : list[datetime.datetime] = []
    
    def _compute_next_due_date(self) -> datetime.datetime:
        """Computes the next due date of the task.

        Returns:
            datetime.datetime: The next due date of the task.
        """
        return self.date_due + self.interval

    def mark_completed(self) -> None:
        """Marks the task as completed."""
        self.completed_dates.append(datetime.datetime.now())
        self.date_due = self._compute_next_due_date()
    
    def __str__(self) -> str:
        return f"{self.title} - Recurring (created: {self.date_created}, due: {self.date_due}, completed: {self.completed_dates}, interval: {self.interval})"
```

``` python
# tasklist.py
from tasks import Task
import datetime

class TaskList:
    def __init__(self, owner: str):
        """Creates a new task list. This contains a list of tasks.

        Args:
            owner (str): Owner of the task list.
        """
        self.owner = owner
        self.tasks: list[Task] = []

    def get_task(self, ix: int) -> Task:
        return self.tasks[ix]

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def remove_task(self, ix: int) -> None:
        del self.tasks[ix]

    def view_tasks(self) -> None:
        print(f"Task list for {self.owner}:")
        print("The following tasks are still to be done:")
        for task in self.uncompleted_tasks:
            # select the appropriate index for the task
            ix = self.tasks.index(task)
            print(f"{ix}: {task}")

    @property 
    def uncompleted_tasks(self) -> list[Task]:
        return [task for task in self.tasks if not task.completed]
```

``` python
# tasks.csv
title,type,date_due,completed,interval,completed_dates,date_created
Buy groceries,Task,03/03/2024,FALSE,,,07/03/2024
Do laundry,Task,09/03/2024,FALSE,,,07/03/2024
Clean room,Task,06/03/2024,FALSE,,,07/03/2024
Do homework,Task,10/03/2024,FALSE,,,07/03/2024
Walk dog,Task,12/03/2024,FALSE,,,07/03/2024
Do dishes,Task,13/03/2024,FALSE,,,07/03/2024
Go to the gym,RecurringTask,07/03/2024,FALSE,"7 days, 0:00:00","2024-02-29,2024-02-22,2024-02-14",08/02/2024
```

Output
``` Console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_6/ToDoApp/main.py
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Edit a task
5. Complete a task
6. Import tasks
7. Export tasks
q. Quit
Enter your choice: 2
Task list for YOUR NAME:
The following tasks are still to be done:
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Edit a task
5. Complete a task
6. Import tasks
7. Export tasks
q. Quit
Enter your choice: 6
Enter the path to the task file: Sessions\session_6\ToDoApp\tasks.csv
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Edit a task
5. Complete a task
6. Import tasks
7. Export tasks
q. Quit
Enter your choice: 2
Task list for YOUR NAME:
The following tasks are still to be done:
0: Buy groceries (created: 2024-03-07 00:00:00, due: 2024-03-03 00:00:00, completed: False)
1: Do laundry (created: 2024-03-07 00:00:00, due: 2024-03-09 00:00:00, completed: False)
2: Clean room (created: 2024-03-07 00:00:00, due: 2024-03-06 00:00:00, completed: False)
3: Do homework (created: 2024-03-07 00:00:00, due: 2024-03-10 00:00:00, completed: False)
4: Walk dog (created: 2024-03-07 00:00:00, due: 2024-03-12 00:00:00, completed: False)
5: Do dishes (created: 2024-03-07 00:00:00, due: 2024-03-13 00:00:00, completed: False)
6: Go to the gym - Recurring (created: 2024-02-08 00:00:00, due: 2024-03-07 00:00:00, completed: [datetime.datetime(2024, 2, 29, 0, 0), datetime.datetime(2024, 2, 22, 0, 0), datetime.datetime(2024, 2, 14, 0, 0)], interval: 7 days, 0:00:00)
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Edit a task
5. Complete a task
6. Import tasks
7. Export tasks
q. Quit
Enter your choice: q
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> 
```