# Session 6 : SOLID and Python Exceptions

## Section 1 SOLID Principles

### Exercise 1: Single Responsibility Principle (SRP)

The Single Responsibility Principle states that a class should have only one responsibility. In the ToDo application, classes such as Task and TaskList follow this principle because they each focus on a single role.

However, the main module violates SRP because it handles user input, output, and business logic. This increases complexity and makes the code harder to maintain. To improve this, I refactored the code by separating responsibilities into different classes, which improves modularity.

### Exercise 2: Open/Closed Principle (OCP)

The Open/Closed Principle states that classes should be open for extension but closed for modification. In the ToDo application, this is achieved by using inheritance.

For example, the RecurringTask class extends the Task class without modifying it:

``` python
class RecurringTask(Task):
    def __init__(self, title, date, interval):
        super().__init__(title, date)
        self.interval = interval
```

This allows new functionality to be added without changing existing code, making the system more flexible.

### Exercise 3: Liskov Substitution Principle (LSP)

The Liskov Substitution Principle ensures that subclasses can replace their parent class without breaking the program.

In this application, RecurringTask can be used wherever a Task is expected because it follows the same structure and behaviour. This ensures consistency and reliability.

### Exercise 4: Interface Segregation Principle (ISP)

The Interface Segregation Principle states that classes should only include methods that are relevant to them.

In the ToDo application, both Task and RecurringTask only contain necessary methods. There are no unnecessary methods that would force subclasses to implement functionality they do not use, keeping the design clean.

### Exercise 5: Dependency Inversion Principle (DIP)

The Dependency Inversion Principle states that high-level modules should depend on abstractions rather than concrete implementations.

In this application, the TaskList class uses DAO classes to manage data storage instead of handling file operations directly. This reduces coupling and allows the storage system to be changed without affecting other parts of the program.

## Section 2 Exception Handling

### Exercise 6: Handling Invalid User Input

In this exercise, I implemented exception handling to manage errors caused by invalid user input.

I used a try-except block to catch IndexError when a user tries to access a task that does not exist:

``` python
try:
    task = task_list.get_task(ix)
    task.mark_completed()
except IndexError:
    print("Task does not exist. Please try again.")
```

This prevents the program from crashing and ensures that the user receives clear feedback. It improves both usability and robustness.

## Section 3: Putting it Together for the ToDoApp

### Exercise 7: Separation of Concerns

Initially, the main module handled multiple responsibilities, which violated the Single Responsibility Principle. To improve this, I refactored the application by separating concerns.

I created a CommandLineUI class to handle user interaction:

``` python
class CommandLineUI:
    def run(self):
        self._print_menu()
```

I also created a TaskManagerController class to handle business logic:

``` python
class TaskManagerController:
    def add_task(self, title, date):
        task = TaskFactory.create_task(title, date)
        self.task_list.add_task(task)
```

This separation reduces coupling and improves maintainability. It also makes the system easier to extend in the future.