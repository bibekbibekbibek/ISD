# Session 4 : Inheritance and Polymorphism

## Section 1 Inheritance

### Exercise 1 Task 1: Simple Inheritance

``` python
class Vehicle:
    def __init__(self, colour, weight, max_speed, form_factor):
        self.colour = colour
        self.weight = weight
        self.max_speed = max_speed
        self.form_factor = form_factor

    def move(self):
        print(f"The Car is driving at {self.max_speed} km/h")
        print(f"The Car is {self.weight} kg in weight")

car = Vehicle("Red", 1500, 200, "Toyota")
car.move()
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_5/lab_week5.py
The Car is driving at 200 km/h
```

### Exercise 1 Task 2: Super() function
Task: Change the move method of the electric and petrol cars to include the maximum range of the vehicle.
For example, the move method of the electric car could print "The electric car is driving at 100 km/h and
has a maximum range of 100 km".
Then modify the code that creates the electric and petrol car objects to include the maximum range
parameter. Run the code and see if your changes work as expected.

``` python  
class Vehicle:
    def __init__(self, colour, weight, max_speed, form_factor):
        self.colour = colour
        self.weight = weight
        self.max_speed = max_speed
        self.form_factor = form_factor

    def move(self):
        print(f"The vehicle is driving at {self.max_speed} km/h")


class Car(Vehicle):
    def __init__(self, colour, weight, max_speed, form_factor):
        super().__init__(colour, weight, max_speed, form_factor)

    def move(self):
        print(f"The car is driving at {self.max_speed} km/h")


class Electric(Car):
    def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, max_range):
        super().__init__(colour, weight, max_speed, form_factor)
        self.battery_capacity = battery_capacity
        self.max_range = max_range

    def move(self, speed):
        print(f"The electric car is driving at {speed} km/h and has a maximum range of {self.max_range} km")


class Petrol(Car):
    def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, max_range):
        super().__init__(colour, weight, max_speed, form_factor)
        self.fuel_capacity = fuel_capacity
        self.max_range = max_range

    def move(self, speed):
        print(f"The petrol car is driving at {speed} km/h and has a maximum range of {self.max_range} km")


electric_car = Electric("Blue", 1800, 250, "Tesla", 100, 100)
electric_car.move(110)

petrol_car = Petrol("Red", 2000, 200, "Ford", 60, 650)
petrol_car.move(180)
```

Output
``` Console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_5/lab_week5.py
The electric car is driving at 110 km/h and has a maximum range of 100 km
The petrol car is driving at 180 km/h and has a maximum range of 650 km
```



### Exercise 1 Task 3 : **kwargs

Task: Change the code so that it now also includes the child class of Vehicle: Plane with its additional
child classes Propeller and Jet. Ensure that the move method of each class derived from Plane says
"Fly" instead of "Drive". Additionally, add a wingspan attribute to the Plane class, a
propeller_diameter attribute to the Propeller class and an engine_thrust attribute to the Jet
class. Ensure that you can create objects of each class and that the attributes are set correctly. 

``` python
class Vehicle:
    def __init__(self, colour, weight, max_speed, form_factor):
        self.colour = colour
        self.weight = weight
        self.max_speed = max_speed
        self.form_factor = form_factor

    def move(self):
        print(f"The vehicle is driving at {self.max_speed} km/h")

class Plane(Vehicle):
    def __init__(self, wingspan, **kwargs):
        super().__init__(**kwargs)
        self.wingspan = wingspan

    def move(self):
        print(f"The plane is flying at {self.max_speed} km/h with a wingspan of {self.wingspan} meters")

class Propeller(Plane):
    def __init__(self, propeller_diameter, **kwargs):
        super().__init__(**kwargs)
        self.propeller_diameter = propeller_diameter

    def move(self):
        print(f"The propeller plane is flying at {self.max_speed} km/h with a wingspan of {self.wingspan} meters and a propeller diameter of {self.propeller_diameter} meters")

class Jet(Plane):
    def __init__(self, jet_engine_thrust, **kwargs):
        super().__init__(**kwargs)
        self.jet_engine_thrust = jet_engine_thrust

    def move(self):
        print(f"The jet plane is flying at {self.max_speed} km/h with a wingspan of {self.wingspan} meters and a jet engine thrust of {self.jet_engine_thrust} kN")

propeller_plane = Propeller(wingspan=30, propeller_diameter=5, colour="White", weight=5000, max_speed=300, form_factor="Boeing")
propeller_plane.move()

jet_plane = Jet(wingspan=35, jet_engine_thrust=200, colour="Silver", weight=8000, max_speed=900, form_factor="Airbus")
jet_plane.move()
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_5/lab_week5.py
The propeller plane is flying at 300 km/h with a wingspan of 30 meters and a propeller diameter of 5 meters
The jet plane is flying at 900 km/h with a wingspan of 35 meters and a jet engine thrust of 200 kN
```

## Section 2 Multiple Inheritance 

### Exercise 2 Task 1: Multiple Inheritance 

``` Python
class Vehicle:
    def __init__(self, colour, weight, max_speed, form_factor, **kwargs):
        self.colour = colour
        self.weight = weight
        self.max_speed = max_speed
        self.form_factor = form_factor

        for key, value in kwargs.items():
            setattr(self, key, value)

    def move(self):
        print(f"The vehicle is moving at {self.max_speed} km/h")

class Car(Vehicle):
    def __init__(self, colour, weight, max_speed, form_factor, **kwargs):
        super().__init__(colour=colour, weight=weight, max_speed=max_speed, form_factor=form_factor, **kwargs)

    def move(self):
        print(f"The car is driving at {self.max_speed} km/h")

class Plane(Vehicle):
    def __init__(self, wingspan, **kwargs):
        super().__init__(**kwargs)
        self.wingspan = wingspan

    def move(self):
        print(f"The plane is flying at {self.max_speed} km/h with a wingspan of {self.wingspan} meters")

class FlyingCar(Car, Plane):
    def __init__(self, colour, weight, max_speed, form_factor, wingspan, **kwargs):
        super().__init__(colour=colour, weight=weight, max_speed=max_speed, form_factor=form_factor, wingspan=wingspan, **kwargs)

    def move(self, speed):
        print(f"The flying car is moving at {speed} km/h with a wingspan of {self.wingspan} meters")
        
flying_car = FlyingCar(colour="Red", weight=1500, max_speed=200, form_factor="Futuristic", wingspan=20)
flying_car.move(100)
```

Output
``` Console 
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_5/lab_week5.py
The flying car is moving at 100 km/h with a wingspan of 20 meters
```

## Section 3 Polymorphism 

### Exercise 3 Task 1 : Polymorphism 

``` python
class Animal:
    def move(self):
        print("The animal is moving")

class Dog(Animal):
    def move(self):
        print("The dog is running")

class Bird(Animal):
    def move(self):
        print("The bird is flying")

class Fish(Animal):
    def move(self):
        print("The fish is swimming")

animals = [Animal(), Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
```

Output
``` Console 
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_5/lab_week5.py
The animal is moving
The dog is running
The bird is flying
The fish is swimming
```

## Section 4 ToDO

### Exercise 4 Task 1 : Tasks

Task: Modify choice "1" in the main function to allow the user to add a recurring task. For this, you should:
- ask the user whether they want to add a recurring task or a normal task
- if they want to add a recurring task, ask them to input a timedelta object in days. You can do this by
asking them to input a number and use this: interval = datetime.timedelta(days=int(interval)) to
convert the number to a timedelta object.
- then create a RecurringTask object and add it to the task list
- change the conditional that if it is simply a normal task, create a Task object and add it to the task list 

``` python
# main.py
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
```

``` python
# tasks.py
import datetime


class Task:

    def __init__(self, title: str, description: str, due_date: datetime.date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.date_created = datetime.datetime.now()

    def mark_completed(self):
        self.completed = True

    def change_title(self, new_title: str):
        self.title = new_title

    def change_description(self, new_description: str):
        self.description = new_description

    def change_due_date(self, new_due_date: datetime.date):
        self.due_date = new_due_date

    def __str__(self):
        return f"{self.title} | Due: {self.due_date} | Completed: {self.completed}"


class RecurringTask(Task):

    def __init__(self, title: str, description: str, due_date: datetime.date, interval: datetime.timedelta):
        super().__init__(title, description, due_date)
        self.interval = interval
        self.completed_dates = []

    def _compute_next_due_date(self):
        return self.due_date + self.interval

    def mark_completed(self):

        current_date = datetime.datetime.now()
        self.completed_dates.append(current_date)

        self.due_date = self._compute_next_due_date()

    def __str__(self):
        completed = ", ".join([d.strftime("%Y-%m-%d") for d in self.completed_dates])
        return f"{self.title} (Recurring) | Due: {self.due_date} | Completed dates: {completed}"
```

``` python
# tasklist.py
import datetime
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
            print("Task not found.")

    def get_task(self, ix: int):
        if 0 <= ix < len(self.tasks):
            return self.tasks[ix]
        else:
            print("Task not found.")
            return None

    def view_tasks(self):

        if not self.tasks:
            print("No tasks available.")
            return

        for i, task in enumerate(self.tasks):
            print(f"{i}. {task}")

    def list_options(self):
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. View Overdue Tasks")
        print("5. Mark Task as Completed")
        print("6. Exit")

    def view_overdue_tasks(self):

        today = datetime.date.today()

        overdue_tasks = [
            task for task in self.tasks
            if task.due_date < today and not task.completed
        ]

        if overdue_tasks:
            print("\nOverdue Tasks:")
            for task in overdue_tasks:
                print(task)
        else:
            print("No overdue tasks.")
```

Output
``` Console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_5/ToDoApp/main.py
Enter task list owner: Bibek

Options:
1. Add Task
2. View Tasks
3. Remove Task
4. View Overdue Tasks    
5. Mark Task as Completed
6. Exit
Enter choice: 1
Enter task title: Java
Enter description: qwerty
Enter due date (YYYY-MM-DD): 2026-3-30
Is this a recurring task? (y/n): y
Enter interval in days: 2

Options:
1. Add Task
2. View Tasks
3. Remove Task
4. View Overdue Tasks
5. Mark Task as Completed
6. Exit
Enter choice: 2
0. Weekly Exercise (Recurring) | Due: 2026-03-11 | Completed dates: 2026-03-04, 2026-02-25, 2026-02-17
1. Java (Recurring) | Due: 2026-03-30 | Completed dates:

Options:
1. Add Task
2. View Tasks
3. Remove Task
4. View Overdue Tasks
5. Mark Task as Completed
6. Exit
Enter choice: 4
No overdue tasks.

Options:
1. Add Task
2. View Tasks
3. Remove Task
4. View Overdue Tasks
5. Mark Task as Completed
6. Exit
Enter choice: 5
Enter task number to mark completed: 1
Task marked as completed

Options:
1. Add Task
2. View Tasks
3. Remove Task
4. View Overdue Tasks
5. Mark Task as Completed
6. Exit
Enter choice: 3
Enter task number to remove: 1

Options:
1. Add Task
2. View Tasks
3. Remove Task
4. View Overdue Tasks
5. Mark Task as Completed
6. Exit
Enter choice: 6
Goodbye
```

### Exercise 4 Task 2 : Encapsulation

Task: Add a method to the TaskList class that allows us to access the tasks in a more controlled way. For
this, you should:
- Modify the TaskList class to include a method called get_task that takes an index as a parameter
and returns the task at that index.
- Modify the main function to use this method instead of accessing the tasks directly. 

``` python
# main.py
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
```

``` python
# tasks.py
class Task:

    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.description} [{status}]"
```

``` python
# tasklist.py
from tasks import Task

class TaskList:

    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task index.")

    def get_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        else:
            print("Invalid task index.")
            return None
        
    def list_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Pending"
                print(f"{i}. {task.description} - {status}")
```

Output
``` Console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_5/ToDoApp/main.py

ToDo List Menu
1. Add Task
2. Remove Task
3. List Tasks
4. Mark Task as Completed
5. View Task
6. Exit
Enter your choice: 1     
Enter task description: Qwerty

ToDo List Menu
1. Add Task
2. Remove Task
3. List Tasks
4. Mark Task as Completed
5. View Task
6. Exit
Enter your choice: 3
0. Qwerty - Pending

ToDo List Menu
1. Add Task
2. Remove Task
3. List Tasks
4. Mark Task as Completed
5. View Task
6. Exit
Enter your choice: 4
Enter task index to mark as completed: 0
Task marked as completed.

ToDo List Menu
1. Add Task
2. Remove Task
3. List Tasks
4. Mark Task as Completed
5. View Task
6. Exit
Enter your choice: 5
Enter task index to view: 0
Task: Qwerty - Completed

ToDo List Menu
1. Add Task
2. Remove Task
3. List Tasks
4. Mark Task as Completed
5. View Task
6. Exit
Enter your choice: 6
Goodbye!
```