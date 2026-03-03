# Session 3 : Python Functions, Scope and Errors

## Section 1 Functions and Scope

### Exercise 1 Task 1 : Functions in Python

``` Python
# Greeting Message
friend_list = ["Bibek", "Prabin", "Anil"]

def greet(friend):
    print(f"Hello {friend}")

for friends in friend_list:
    greet(friends)
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_3/lab_week_3.py
Hello Bibek
Hello Prabin
Hello Anil
```

``` python 
#Tax Calculation
def calculate_tax(income, tax_rate):
    tax = income * tax_rate
    return tax  

calculated_tax = calculate_tax(100000, 0.5)
print("Calculated Tax:", calculated_tax, "pounds")
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_3/lab_week_3.py
Calculated Tax: 50000.0 pounds
``` 

``` python
# Compound Interest Calculator Function
def compound_interest(principal, duration, interest_rate):
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None
    if duration < 0:
        print("Please enter a positive number of years")
        return None
    for year in range(1, duration + 1):
        total_for_the_year = principal * (1 + interest_rate) ** year
        print(f"The total amount of money earned by the investment in year {year} is {total_for_the_year:.2f} pounds")
    final_amount = principal * (1 + interest_rate) ** duration
    return int(final_amount)

result = compound_interest(1000, 5, 0.05)
print("Final amount:", result)
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_3/lab_week_3.py
The total amount of money earned by the investment in year 1 is 1050.00 pounds.
The total amount of money earned by the investment in year 2 is 1102.50 pounds.
The total amount of money earned by the investment in year 3 is 1157.63 pounds.
The total amount of money earned by the investment in year 4 is 1215.51 pounds.
The total amount of money earned by the investment in year 5 is 1276.28 pounds.
Final amount: 1276
```

### Exercise 2 Task 2 : Variable Scope

``` python
def new_function():
my_new_variable = 5
new_function() # call the function. No problems here.
print(my_new_variable) # this will cause an error
```

``` python
my_new_variable = 0

def new_function():
    my_new_variable = 5

new_function()

print(my_new_variable)

# A variable defined outside a function is global, while a variable with the same name inside a function is local, and they are two separate variables with different scopes.
```

## Section 2 Assertions and Errors

### Exercise 1 Task 1 : Assertions

``` python
# Write a code line in the format assertion, expression, message where the expression is true.
# Write a second code line where the expression is false and see the assertion error.

assert 2 + 2 == 4, "This assertion should pass because 2 + 2 equals 4."
assert 2 + 2 == 5, "This assertion should fail because 2 + 2 does not equal 5."
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_3/lab_week_3.py
Traceback (most recent call last):
  File "c:\Users\raibi\OneDrive\Documents\Python-ISD26\Sessions\session_3\lab_week_3.py", line 45, in <module>
    assert 2 + 2 == 5, "This assertion should fail because 2 + 2 does not equal 5."
           ^^^^^^^^^^
AssertionError: This assertion should fail because 2 + 2 does not equal 5.
```

### Exercise 1 Task 2 : Identifying and Fixing Common Errors
``` python

# 1. Syntax Error
# print("Hello, World!"  # Missing closing parenthesis

print ("Hello, World!")  # Fixed syntax error

# 2. Name Error
# print(greeting)  # 'greeting' is not defined

greeting = "Hello, World!"
print(greeting)  # Fixed name error

# 3. Value Error
# number1 = "5"
# number2 = 3
# result = number1 + number2
# print("The sum is:", result) # This will raise a ValueError because you cannot add a string and an integer.

number1 = "5"
number2 = 3
result = int(number1) + number2
print("The sum is:", result)

# 4 Index Error
my_list = [1, 2, 3]
print(my_list[3])  # This will raise an IndexError because there is no index 3 in the list (indices are 0, 1, and 2).

# 5 Indentation Error
# def greet():
# print("Hello, World!")  # This line is not indented properly

def greet():
    print("Hello, World!")  # Fixed indentation error
```


## Section 3 Your first larger-scale Python programme

``` python
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
```

Output 
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_3/to_do_week_3.py

To-Do List Manager
1. Add a new task        
2. View current tasks    
3. Remove a task
4. Quit
Enter your choice (1-4): 1
Enter a new task: Java
Task added successfully!

To-Do List Manager
1. Add a new task
2. View current tasks
3. Remove a task
4. Quit
Enter your choice (1-4): 1
Enter a new task: Python
Task added successfully!

To-Do List Manager
1. Add a new task
2. View current tasks
3. Remove a task
4. Quit
Enter your choice (1-4): 1   
Enter a new task: HTML
Task added successfully!

To-Do List Manager
1. Add a new task
2. View current tasks
3. Remove a task
4. Quit
Enter your choice (1-4): 1
Enter a new task: PHP
Task added successfully!

To-Do List Manager
1. Add a new task
2. View current tasks
3. Remove a task
4. Quit
Enter your choice (1-4): 2
Current tasks:
1. Java
2. Python
3. HTML
4. PHP

To-Do List Manager
1. Add a new task
2. View current tasks
3. Remove a task
4. Quit
Enter your choice (1-4): 3
Current tasks:
1. Java
2. Python
3. HTML
4. PHP
Enter the number of the task to remove: 4
Task 'PHP' removed successfully!

To-Do List Manager
1. Add a new task
2. View current tasks
3. Remove a task
4. Quit
Enter your choice (1-4): 2
Current tasks:
1. Java
2. Python
3. HTML

To-Do List Manager
1. Add a new task
2. View current tasks
3. Remove a task
4. Quit
Enter your choice (1-4): 4
Exiting the program. Goodbye!
```

