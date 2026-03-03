# # Task1 : Greeting message

friend_list = ["Bibek", "Prabin", "Anil"]

def greet(friend):
    print(f"Hello {friend}")

for friends in friend_list:
    greet(friends)

# # Task2 : Tax calculation

def calculate_tax(income, tax_rate):
    tax = income * tax_rate
    return tax  

calculated_tax = calculate_tax(100000, 0.5)
print("Calculated Tax:", calculated_tax, "pounds")

# # Compound Interest Calculator Function

def compound_interest(principal, duration, interest_rate):
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None
    if duration < 0:
        print("Please enter a positive number of years")
        return None
    for year in range(1, duration + 1):
        total_for_the_year = principal * (1 + interest_rate) ** year
        print(f"The total amount of money earned by the investment in year {year} is {total_for_the_year:.2f} pounds.")
    final_amount = principal * (1 + interest_rate) ** duration
    return int(final_amount)

result = compound_interest(1000, 5, 0.05)
print("Final amount:", result)


# Exercise 1 Task 1 : Assertions

# Write a code line in the format assertion, expression, message where the expression is true.
# Write a second code line where the expression is false and see the assertion error.

assert 2 + 2 == 4, "This assertion should pass because 2 + 2 equals 4."
assert 2 + 2 == 5, "This assertion should fail because 2 + 2 does not equal 5."

# Exercise 1 Task 2 : Identifying and Fixing Common Errors
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