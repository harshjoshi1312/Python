# 1. Write an if statement that checks if a number is positive.
num = 5
if num > 0:
    print("Positive number")

# 2. Write an if-else statement to check if a number is even or odd.
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Write an if-elif-else ladder to categorize age.
age = 18
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

# 4. Write a for loop to print numbers from 1 to 5.
for i in range(1, 6):
    print(i)

# 5. Write a while loop to print numbers from 5 to 1.
i = 5
while i >= 1:
    print(i)
    i -= 1

# 6. Use break statement inside a for loop.
for i in range(1, 10):
    if i == 5:
        break
    print(i)
# Stops when i == 5

# 7. Use continue statement inside a for loop.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Skips 3

# 8. Write a nested if to check if a number is positive and even.
num = 8
if num > 0:
    if num % 2 == 0:
        print("Positive and Even")

# 9. Write a for loop to print all characters of a string.
text = "Hello"
for char in text:
    print(char)

# 10. Use pass statement inside a function.
def my_function():
    pass
# Placeholder for future code.
