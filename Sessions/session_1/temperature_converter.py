# Section 3: First Program in Python

# Requirements:
# • The user stores the Celsius value as a number in a variable called celsius_input
# • The Celsius value then gets converted to Fahrenheit and stored in a variable called 
# degree_f
# • The Celsius value then gets converted to Kelvin and stored in a variable called degree_k
# • (Note: Use the internet to find out the formulas on how to convert C to K and F and 
# implement that using Python operators
# • Generate and print an output that follows the following format:

celsius_input = 25
degree_f = (float(celsius_input) * 9/5) + 32
degree_k = float(celsius_input) + 273.15   
output = f"The Celsius value is: {celsius_input}°C\nThe Fahrenheit value is: {degree_f}°F\nThe Kelvin value is: {degree_k}K"
print(output)
