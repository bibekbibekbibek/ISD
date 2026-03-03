# Exercise 1 Task: Variables and Types
var_1 = True # Type:'bool'
var_2 = 1 # Type:'int'
var_3 = 3.14159  # Type:'float'
var_4 = "Hello, World!" # Type:'str'

print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

# Exercise 1 Task: Casting Variables
my_int = 5
my_float = 5.5
my_bool = True
print("my_int = ", my_int, "my_float = ", my_float, "my_bool = ", my_bool)

my_int_float = float(my_int)
print("my_int_float = ", my_int_float)

my_float_int = int(my_float)
print("my_float_int = ", my_float_int)

my_bool_int = int(my_bool)
print("my_bool_int = ", my_bool_int)




# Exercise 2 Arithmetic operators

#Addition
result_addition = 10 + 5 
print("Addition:", result_addition)

#Subtraction
result_subtraction = 20-8
print("Subtraction:", result_subtraction)

#Multiplication
result_multiplication = 6*4 
print("Multiplication:", result_multiplication)

#Division
result_division = 15 / 3 
print("Division:", result_division)

#Floor Division
result_floor_division = 17 // 4 
print("Floor Division:", result_floor_division)

#Modulus
result_modulus = 17 % 4 
print("Modulus:", result_modulus)

#Exponentiation
result_exponentiation = 2 ** 3 
print("Exponentiation:", result_exponentiation)


# Task 2: Calculating the Average:

num1 = 10
num2 = 20
Average = (num1 + num2) / 2
print("the num1 is:", num1)
print("the num2 is:", num2)
print("The average of", num1, "and", num2, "is:", Average)


# Task 3: Calculate the Area of a Rectangle:

length = 5
width = 3
area = length * width
print("The length of the rectangle is:", length)    
print("The width of the rectangle is:", width)
print("The area of the rectangle is:", area)


# Task 1: Modify Strings:

# 1. Create a new variable called my_string and store the following in it: “This class covers ISD.”
# 2. Print the my_string variable
# 3. Using the documentation in the link above, look through the examples and do the following:
# a. Create a new variable my_uppercase_string that stores the my_string converted to 
# uppercase
# b. Create a new variable my_lowercase_string that stores the my_string converted to 
# lowercase
# c. Create a new variable my_new_string that replaces the word “ISD” in the string with 
# “Interactive Software Design”.
# d. Create a new variable my_string_length that stores the length of the string (Note: use a 
# search engine or the lecture slides to help you how to do this).

my_string = "This class covers ISD."
print("The my_string is:", my_string)

my_uppercase_string = my_string.upper()
print("The my_uppercase_string is:", my_uppercase_string)

my_lowercase_string = my_string.lower()
print("The my_lowercase_string is:", my_lowercase_string)

my_new_string = my_string.replace("ISD", "Interactive Software Design")
print("The my_new_string is:", my_new_string)

my_string_length = len(my_string)
print("The my_string_length is:", my_string_length)


# Task 2: f-Strings
# 1. Create variables called my_name, number_of_classes, campus. Store your name, the number of 
# classes you are taking this term and then the campus you are studying at.
# 2. Create an f-string using the instructions above called my_text that combines the text to the 
# following scheme. (Example: my_name = Peter, number of classes = 10, campus = Paisley):
# “My name is Peter and I am studying 10 classes in Paisley”.
# 3. Print the string, run the program, and ensure that you have done everything correctly.

my_name = "Bibek Rai"
my_number_of_classes = 3
my_campus = "Paisley Campus"

my_text = f"My name is {my_name} and I am studying {my_number_of_classes} classes in {my_campus}"
print(my_text)



