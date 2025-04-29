# 1. Declare two variables, x and y, and assign them values 10 and 5 respectively.
x = 10
y = 5
# Variables are created by just assigning values; no need to declare types in Python.

# 2. What is the data type of the variable x?
print(type(x))  # Output: <class 'int'>

# 3. Convert the integer x to a float.
x_float = float(x)
print(x_float)  # Output: 10.0

# 4. Take input from the user and print it.
user_input = input("Enter something: ")
print("You entered:", user_input)
# Note: input() always returns a string.

# 5. Add two numbers taken from user input.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# 6. Use a single line comment and a multi-line comment.
# This is a single line comment
"""
This is a
multi-line comment
"""

# 7. Use arithmetic operators to calculate the square of a number.
n = 4
print("Square:", n * n)  # or n ** 2

# 8. Find the remainder when 10 is divided by 3.
print(10 % 3)  # Output: 1

# 9. Use the type() function to check types of various variables.
s = "Hello"
f = 3.14
print(type(s))  # <class 'str'>
print(type(f))  # <class 'float'>

# 10. Use formatted string (f-string) to print a message.
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")
