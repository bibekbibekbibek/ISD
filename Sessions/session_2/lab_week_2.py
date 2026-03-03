# Exercise 1: Comparison Operators

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

# Exercise 2: Logical Operators

x = 20
print(x > 10 and x < 30)

print(x > 30 or x < 10)

print(not (x > 15))


# Exercise 3: if Conditions

age = 19
age_group = "child"

if age >= 18:
    age_group = "adult"

print(f"the age group is {age_group}")

age = 17
age_group = "child"

if age >= 18:
    age_group = "adult"

print(f"the age group is {age_group}")

# Exercise 4: if-else Conditions

wind_speed = 30
if wind_speed < 10:
    print("It's a calm day!")
else:
    print("It's a windy day!")

wind_speed = 9
if wind_speed < 10:
    print("It's a calm day!")
else:
    print("It's a windy day!")

# Exercise 5: if-elif-else Conditions

grade = 50
if grade < 30:
    print("you failed")
elif grade <= 40:
    print("you passed")
elif grade <= 50:
    print("you got a good grade")
else:
    print("you got an excellent grade")

# Exercise 6: Summary Tasks
# compare two temperatures

Temperature1 = 25
Temperature2 = 30
if Temperature1 == Temperature2:
    print("The temperatures are equal.")
else:
    print("The temperatures are not equal.")

# Exercise 1: Creating a list

city_list = ["Glasgow", "London", "Edinburgh"]
print("City List:", city_list)

# Exercise 2: Accessing List Elements

print("Third city:", city_list[2])
print("last two cities:", city_list[1:3])

# Exercise 3: Modifying a List

city_list.append("Manchester")
print("Updated City List:", city_list)

city_list[1] = "Birmingham"
print("Modified City List:", city_list)


# Exercise 4: Summary Tasks

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

# Exercise 1: While loop
i=0
while i < 5:
    print(i)
    i += 1

# Exercise 2: For loop
city_list = ["Glasgow", "London", "Edinburgh"]
for city in city_list:
    print(city)

# Exercise 3: Loop Keywords: Range, Break and Continue

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

# Task – Sum of Squares
# 1. Create a variable sum_of_squares and initialize it to 0.
# 2. Use a for loop to iterate through the numbers from 1 to 5 (inclusive) using the range() function.
# 3. Add the square of each number to sum_of_squares.
# 4. Print the final value of sum_of_squares. (Hint: if you do it correctly, the result should be 55)

sum_of_squares = 0
for num in range(1, 6):
    sum_of_squares += num ** 2
print("The sum of squares from 1 to 5 is:", sum_of_squares)

# Task – Countdown:
# 1. Create a variable countdown and initialize it to 10.
# 2. Use a while loop to print a countdown from the value of countdown to 1.
# 3. After the countdown, print "Liftoff!"

countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Liftoff!")



# Task 1: User Input and Conditional Statements
# Write a code that takes the user's age as input. If the age is less than 18, print "You are a minor." If the
# age is between 18 and 65 (inclusive), print "You are an adult." If the age is greater than 65, print "You are
# a senior citizen."

age = int(input("Please enter your age: "))
if age < 18:
    print("You are a minor.")
elif age >= 18 and age <= 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")  


# Task 2: Temperature Converter

celsius_input = input("Enter a temperature in Celsius: ")
degree_f = (float(celsius_input) * 9/5) + 32
degree_k = float(celsius_input) + 273.15   
output = f"The Celsius value is: {celsius_input}°C\nThe Fahrenheit value is: {degree_f}°F\nThe Kelvin value is: {degree_k}K"
print(output)