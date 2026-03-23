# Session 4 : Debugging, Properties and Persistence

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