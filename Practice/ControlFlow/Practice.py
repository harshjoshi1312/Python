# 1. Write an if statement that checks if a variable "score" is greater than 50.
score = 30
if score > 50:
    print("Score is greater than 50")



# 2. Write an if-else that checks if a string "password" is equal to "admin".
password = "admin123"
if password == "admin":
    print("Access granted")

# 3. Write an if-elif-else ladder to print "small", "medium", or "large" based on a number.
number = 15

if number < 10:
    print("small")
elif number < 20:
    print("medium")
else:
    print("large")

# 4. Use a for loop to print numbers from 10 to 1. // wow this is a good one
for i in range(10, 0, -1):
    print(i)



# 5. Use a while loop to print even numbers from 2 to 10.
i = 2
while i <= 10:
    print(i)
    i += 2

# 6. Use break inside a while loop when a number reaches 5.
i =1 
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1



# 7. Use continue inside a for loop to skip printing number 4.
j = 2
while j <= 10:
    if j ==4 :
      continue    
    print(j)
    j += 1



# 8. Write a nested if-else to check if a number is between 10 and 20.
number = 15
if number > 10:
    if number < 20:
        print("Number is between 10 and 20")
    else:
        print("Number is greater than or equal to 20")
else:
    print("Number is less than or equal to 10")


# 9. Write a for loop to print every letter of the word "Python".
str = "Python"
for i in str:
    print(i)



# 10. Write a while loop that prints numbers from 0 to 4.
x = 0
while x < 5:
    print(x)
    x += 1

# 11. Create a loop that prints "Done" after completing.
for i in range(5):
    print(i)
print("Done")  # This will print "Done" after the loop completes.


# 12. Use else with a while loop and print a message when the loop finishes normally.
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished normally")
# This will print "Loop finished normally" after the while loop completes.

# 13. Use else with a for loop and print "Loop completed".
i = 10
for i in range(5):
    print(i)
else:
    print("Loop completed")

# 14. Check if a number is divisible by both 2 and 3.

num = 6
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")

# 15. Check if a number is divisible by either 2 or 3.
num 8 
if num % 2 == 0 or num % 3 == 0:
    print("Divisible by either 2 or 3")

# 16. Find the largest among three numbers using if-else.
num1 = 10
num2 = 20
num3 = 15

if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)

# 17. Check if a year is a leap year (divisible by 4 and not by 100 unless divisible by 400).
year = 2020
if (year % 4 == 0 and year %100 != 0) or (year % 400 == 0):
    print("Leap year")

# 18. Create a simple menu (1 for Pizza, 2 for Burger, 3 for Exit) using if-elif-else.
menu = int(input("Enter 1 for Pizza, 2 for Burger, 3 to Exit: "))
if menu == 1:
    print("You chose Pizza")
elif menu == 2:
    print("You chose Burger")
elif menu == 3:
    print("Exiting...")
else:
    print("Invalid choice")


# 19. Use a loop to calculate the sum of first 5 natural numbers.
sum = 0
for i in range(1, 6):
    sum += i
print("Sum of first 5 natural numbers is:", sum)



# 20. Use a loop to calculate the factorial of a number. // wao this is a good one 
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)



# 21. Write a loop that counts down from 5 to 0.
g = 5
while g >= 0:
    print(g)
    g -= 1


# 22. Use a nested loop to print a pattern like: // i have to recheck this one 
# *
# **
# ***
# ****
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()  # Move to the next line after each row


# 23. Use range to print odd numbers between 1 and 10. //in the for loop you can pass the limit also for the attreations 
for i in range(1, 11, 2):
    print(i)



# 24. Write a loop that stops if user inputs "exit". // recehck this one 
user_input = ""
while user_input.lower() != "exit":
    user_input = input("Type 'exit' to stop: ")
    if user_input.lower() == "exit":
        print("Exiting...")
    else:
        print("You entered:", user_input)

# 25. Write an infinite loop and break when a condition is met.
i = 0
while True:
    print(i)
    i += 1
    if i == 5:
        break  # Breaks the loop when i equals 5

# 26. Print numbers 1 to 20 skipping multiples of 3.
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)

# 27. Write code that checks if a number is negative, zero, or positive.
num = -5
if num < 0:
    print("Negative")
elif num == 0:
    print("Zero")
else:
    print("Positive")

# 28. Write a for loop that prints multiples of 5 up to 50.
for i in range(5, 51, 5):
    print(i)


# 29. Create a guessing game using while loop (guess a number).
nume = 7
guess = 0
while guess != nume:
    guess = int(input("Guess the number (1-10): "))
    if guess < nume:
        print("Too low!")
    elif guess > nume:
        print("Too high!")
    else:
        print("Correct!")

# 30. Use a loop to reverse a string. // i have to check this aslo
string = "Hello"
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)  # Output: "olleH"

# 31. Find the sum of digits of a number using while loop. // have to chek this also
num = 12345
while num > 0 :
    digit = num % 10
    num //= 10
    print(digit)  # Output: 5, 4, 3, 2, 1 (in reverse order)

# 32. Find the product of digits of a number using while loop.
Nummer = 12345
product = 1
while Nummer > 0:
    digit = Nummer % 10
    product *= digit
    Nummer //= 10
print("Product of digits:", product)  # Output: 120 (1*2*3*4*5)

# 33. Print the Fibonacci series up to n terms.
None = 10
n1, n2 = 0, 1
print("Fibonacci series:")
for i in range(None):
    print(n1, end=" ")
    nth = n1 + n2
    n1 = n2
    n2 = nth



# 34. Print all prime numbers between 1 and 20.
# i have to check this also
for num in range(2, 21):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# 35. Find the GCD (Greatest Common Divisor) of two numbers using loop.

num1 = 48
num2 = 18
gcd = 1
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print("GCD of", num1, "and", num2, "is:", gcd)  # Output: 6 (GCD of 48 and 18)






# 36. Find the LCM (Least Common Multiple) of two numbers using loop.
num1 = 4
num2 = 6
lcm = 1
for i in range(1, (num1 * num2) + 1):
    if i % num1 == 0 and i % num2 == 0:
        lcm = i
        break
print("LCM of", num1, "and", num2, "is:", lcm)  # Output: 12 (LCM of 4 and 6)

# 37. Use nested ifs to check if a number is divisible by 5 and greater than 10

num = 15
if num > 10:
    if num % 5 == 0:
        print("Number is greater than 10 and divisible by 5")
    else:
        print("Number is greater than 10 but not divisible by 5")
else:
    print("Number is less than or equal to 10") 


# 38. Find the number of vowels in a given string using for loop.
string = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels in the string:", count)  # Output: 3 (e, o, o)



# 39. Use a for loop to iterate over a list of numbers and print their squares.
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    square = num ** 2
    print("Square of", num, "is:", square)  # Output: 1, 4, 9, 16, 25



# 40. Write a for loop that prints a right-angled triangle pattern using numbers.
#
# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()  # Move to the next line after each row

