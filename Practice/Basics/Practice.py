# 1. Declare a variable named "name" and assign your name to it.
name = "harsh"



# 2. Print the value of the variable "name".
print(name)

# 3. Declare three variables in one line with values 1, 2, 3.
x , y ,z = 1 , 2 , 3 

# 4. Find the type of the value 3.5.
x = 3.5
print(type(x))  # Output: <class 'float'>

# 5. Convert the string "123" to an integer.
z = "123"
z1 =int(z)
print(z1)  # Output: 123

# 6. Convert the number 45 to a string and print it.

h = 45
h1 = str(h)
print(h1)  # Output: '45'

# 7. Get input from the user and print its type.
user_inout = input("enter something: ");
print(type(user_inout))  # Output: <class 'str'>    

# 8. Write a single line that adds 2 numbers and prints the result.
print(2 + 3)  # Output: 5

# 9. Declare a variable with a float value and print its square.
xy = 2.5
xy1 = xy * xy
print(xy1)  # Output: 6.25


# 10. Use an f-string to say "Welcome, John!" (assume name is in variable `name`).
names = "harsh" 
print(f"Welcome, {names}!")  # Output: Welcome, harsh!


# 11. Use the `type()` function to check type of `True`.
z = True
print(type(z))  # Output: <class 'bool'>

# 12. Print the result of 5 divided by 2.
print(5 % 2 )  # Output: 1.0

# 13. Print the result of integer division of 5 by 2.
print(5 // 2)  # Output: 2

# 14. Print the result of 2 raised to the power 4.
print(2 ** 4)  # Output: 16

# 15. Use modulo operator to find if 15 is even or odd.
print(15 % 2)  # Output: 1 (odd)


# 16. Declare a constant variable for PI (just use UPPERCASE naming convention).
PI = 3.14
print(PI)  # Output: 3.14


# 17. Add a multi-line comment describing yourself.
""" hey my name is harsh and i am learning python."""

# 18. Print the length of the string "Python".
lenstring = "harsh is here"
print(len(lenstring))  # Output: 14

# 19. Concatenate two strings: "Hello" and "World".
str1 = "hello"
str2 = "world"
str3 = str1 + str2
print(str3)  # Output: helloworld


# 20. Repeat the string "Hi" 3 times.
str4 = "hi"
str5 = str4 * 3
print(str5)  # Output: hihihi


# 21. Assign `None` to a variable and print it.
ab = None
print(ab)  # Output: None

# 22. Declare a boolean variable and print it.
boolvar = False
print(boolvar)  # Output: False

# 23. Convert boolean True to integer.
ac = True
bc = int(ac)
print(bc)  # Output: 1

# 24. Round the float number 3.678 to 2 decimal places.
fnmum = 3.678
print(round(fnmum, 2))  # Output: 3.68

# 25. Use escape characters to print: He said, "I’m learning Python!"
print("He said, \"I’m learning Python!\"")  # Output: He said, "I’m learning Python!"

# 26. Join a list `['a', 'b', 'c']` into a single string.  // wow this is a good question 
list1 = ['a', 'b', 'c']
joined_string = ''.join(list1)
print(joined_string)  # Output: abc

# 27. Slice the string "Python" to get "tho".
slc = "python"
print(slc[2:5])  # Output: tho

# 28. Print the ASCII value of the character 'A'. // wow this is a good question
print(ord('A'))  # Output: 65

# 29. Print the character for ASCII code 97. //for ascii use ord and for the char use chr
# wow this is a good question
print(chr(97))  # Output: a

# 30. Find the max of three numbers: 5, 10, 3.
max_num = max(5, 10, 3)
print(max_num)  # Output: 10


# 31. Check if a number is positive using if-else (basic only).
num = 5
if num > 0:
    print("Positive")
else:
    print("Not Positive")




# 32. Print the absolute value of -10. // for checking the absolute value we cna use the abs
print(abs(-10))  # Output: 10


# 33. Print the memory address of a variable using id(). // variable addreess can be track using the id futnction
x = 10
print(id(x))  # Output: Memory address of x (e.g., 140703123456064)

# 34. Convert string "True" to boolean.
axy = "True"
bxy = bool(axy)
print(bxy)  # Output: True (but note that any non-empty string is True in Python)

# 35. Check if two variables refer to the same object.  // use is opearyor to check the same object
# (use `is` operator)
a = [1, 2, 3]
b = a
print(a is b)  # Output: True (both refer to the same list object)

# 36. Multiply a number by 0 and print the result.
num1 = 10
num2 = num1 * 0
print(num2)  # Output: 0

# 37. Swap two numbers using a single line.
a, b = 5, 10
a, b = b, a
print(a, b)  # Output: 10 5

# 38. Use the `help()` function on the `len` function.

help(len)  # This will display the help documentation for the len function.


# 39. Print the binary, octal, and hexadecimal of number 12.
print(bin(12))  # Output: 0b1100 (binary)
print(oct(12))  # Output: 0o14 (octal)
print(hex(12))  # Output: 0xc (hexadecimal)


# 40. Create a variable with a long integer and print its type.
long_int = 12345678901234567890
print(type(long_int))  # Output: <class 'int'>

