# Session 2: Introduction to Python Programming II

## Section 1 Comparisons and Conditionals

### Exercise 1 Task 1 : Comparison Operators

``` python
a = 10
b = 20
print("a =", a)
print("b =", b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b) 
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
a = 10
b = 20
a == b: False
a != b: True
a > b: False
a < b: True
a >= b: False
a <= b: True
```

### Exercise 1 Task 2 : Logical Operators

``` python
x = 20
print(x > 10 and x < 30)

print(x > 30 or x < 10)

print(not (x > 15))
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
True
False
False
```

### Exercise 1 Task 3 : if Conditions

``` python
age = 19
age_group = "child"

if age >= 18:
    age_group = "adult"

print(f"the age group is {age_group}")
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
the age group is adult
```

``` python
age = 17
age_group = "child"

if age >= 18:
    age_group = "adult"

print(f"the age group is {age_group}")
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
the age group is child
```

### Exercise 1 Task 4 : if-else Conditions

``` python
wind_speed = 30
if wind_speed < 10:
    print("It's a calm day!")
else:
    print("It's a windy day!")
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
It's a windy day!
```

``` python
wind_speed = 9
if wind_speed < 10:
    print("It's a calm day!")
else:
    print("It's a windy day!")
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
It's a calm day!
```

### Exercise 1 Task 5 : if-elif-else Conditions

``` python
grade = 50
if grade < 30:
    print("you failed")
elif grade <= 40:
    print("you passed")
elif grade <= 50:
    print("you got a good grade")
else:
    print("you got an excellent grade")
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
you got a good grade
```

### Exercise 1 Task 6 : Summary Tasks

``` python
# compare two temperatures

Temperature1 = 25
Temperature2 = 30
if Temperature1 == Temperature2:
    print("The temperatures are equal.")
else:
    print("The temperatures are not equal.")
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
The temperatures are not equal.
```

## Section 2 Python Lists

### Exercise 2 Task 1 :  Creating a list

``` python 
city_list = ["Glasgow", "London", "Edinburgh"]
print("City List:", city_list)
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
City List: ['Glasgow', 'London', 'Edinburgh']
```

### Exercise 2 Task 2 : Accessing List Elements

``` python
city_list = ["Glasgow", "London", "Edinburgh"]
print("City List:", city_list)
print("Third city:", city_list[2])
print("last two cities:", city_list[1:3])
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
City List: ['Glasgow', 'London', 'Edinburgh']
Third city: Edinburgh
last two cities: ['London', 'Edinburgh']
```

### Exercise 2 Task 3 : Modifying a list

``` python
city_list = ["Glasgow", "London", "Edinburgh"]
print("City List:", city_list)

city_list.append("Manchester")
print("Updated City List:", city_list)

city_list[1] = "Birmingham"
print("Modified City List:", city_list)
```

Output
```console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
City List: ['Glasgow', 'London', 'Edinburgh']
Updated City List: ['Glasgow', 'London', 'Edinburgh', 'Manchester']     
Modified City List: ['Glasgow', 'Birmingham', 'Edinburgh', 'Manchester']
```

### Exercise 2 Task 4 : Summary Task

``` python
# Task Create, Access and Modify Lists

colours = ["red", "green", "blue"]
print("Colours List:", colours)

colours[0] = "yellow"
print("Updated Colours List:", colours)

len_colours = len(colours)
print("Number of colours:", len_colours)

if "red" in colours:
    print("Red is in the list.")
else:
    print("Red is not in the list.")

selected_colour = colours[1:3]
print("Selected Colours:", selected_colour)
```

Output
```console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
Colours List: ['red', 'green', 'blue']
Updated Colours List: ['yellow', 'green', 'blue']
Number of colours: 3
Red is not in the list.
Selected Colours: ['green', 'blue']
```

## Section 3 Python Loops

### Exercise 3 Task 1 : While Loop

``` python
i=0
while i < 5:
    print(i)
    i += 1
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
0
1
2
3
4
```

### Exercise 3 Task 2 : For Loop

``` python
city_list = ["Glasgow", "London", "Edinburgh"]
for city in city_list:
    print(city)
```

Output 
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
Glasgow
London   
Edinburgh
```

### Exercise 3 Task 2 : Loop Keywords: Range, Break and Continue

``` python
print("For range and break:")
i = 0
for i in range(1, 11):
    if i == 5:
        break
    print(i)

print("For range and continue:")
j = 0
for j in range(1, 11):
    if j == 5:
        continue
    print(j) 
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
For range and break:
1
2
3
4
For range and continue:
1
2
3
4
6
7
8
9
10
```

### Exercise 3 Task 4 : Summary Tasks

``` python
# Task – Even Numbers
# 1. Create a list called numbers which contains the integers from 1 to 10.
# 2. Use a for loop to iterate through the list and only print the even numbers. (Hint: use the modulo
# % operator)
numbers = list(range(1, 11))
print("Numbers List:", numbers)
print("Even Numbers:")
for number in numbers:
    if number % 2 == 0:
        print(number)
```

Output
``` Console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
Numbers List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even Numbers:
2
4
6
8
10
```

``` python
# Task – Sum of Squares
# 1. Create a variable sum_of_squares and initialize it to 0.
# 2. Use a for loop to iterate through the numbers from 1 to 5 (inclusive) using the range() function.
# 3. Add the square of each number to sum_of_squares.
# 4. Print the final value of sum_of_squares. (Hint: if you do it correctly, the result should be 55)
sum_of_squares = 0
for num in range(1, 6):
    sum_of_squares += num ** 2
print("The sum of squares from 1 to 5 is:", sum_of_squares)
```

Output 
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
The sum of squares from 1 to 5 is: 55
```

``` python
# Task – Countdown:
# 1. Create a variable countdown and initialize it to 10.
# 2. Use a while loop to print a countdown from the value of countdown to 1.
# 3. After the countdown, print "Liftoff!"
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Liftoff!")
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
10
9
8
7
6
5
4
3
2
1
Liftoff!
```

## Section 4 Obtaining User Input

### Exercise 4 Task 1 : User Input and Conditional Statements

``` python
age = int(input("Please enter your age: "))
if age < 18:
    print("You are a minor.")
elif age >= 18 and age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
Please enter your age: 30
You are an adult.
```

### Exercise 4 Task 2 : Temperature Converter

``` python
celsius_input = input("Enter a temperature in Celsius: ")
degree_f = (float(celsius_input) * 9/5) + 32
degree_k = float(celsius_input) + 273.15   
output = f"The Celsius value is: {celsius_input}°C\nThe Fahrenheit value is: {degree_f}°F\nThe Kelvin value is: {degree_k}K"
print(output)
```

Output
``` console
PS C:\Users\raibi\OneDrive\Documents\Python-ISD26> & C:/Users/raibi/AppData/Local/Python/pythoncore-3.14-64/python.exe c:/Users/raibi/OneDrive/Documents/Python-ISD26/Sessions/session_2/lab_week_2.py
Enter a temperature in Celsius: 30
The Celsius value is: 30°C     
The Fahrenheit value is: 86.0°F
The Kelvin value is: 303.15K  
```
