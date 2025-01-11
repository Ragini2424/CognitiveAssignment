#1.write a Python program to print "Anything You find cool.
print("Anything you find cool.")


# 2.1 Write a program to add two numbers and print the result.
print(3+4)
# 2.2 Write a program to concatenate two strings and print the result.
print("hello"+""+"world")
#2.3 Write a program to concatenate a string and a number and print the result.
print("ragini"+""+str(24))


#3.1 Write a Python program to check if a number is positive, negative, or zero using an if-else statement.
number = 24
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#3.2 Write a program to check if a given number is odd or even.
number = 23
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


#4.1 Write a program to print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

#4.2 Write a program to print numbers from 1 to 10 using a while loop.
i=1
while(i<=10):
    print(i)
    i=i+1

#4.3 Write a program to calculate the sum of numbers from 1 to 100 using a loop. 
sm=0
for i in range(1,101):
    sm=sm+i
print(sm)

#5.1 Create a list of 5 numbers. Write a program to find the largest and smallest numbers in the list.
numbers = [23, 45, 12, 67, 34]
print("The largest number is:", max(numbers))
print("The smallest number is:", min(numbers))

#5.2 Create a dictionary with at least 3 key-value pairs. Write a program to retrieve the value of a given key.

dict = {"name": "Alice", "age": 25, "city": "New York"}
key="name"
print(dict[key])

#5.3 Write a program to sort a list of numbers in ascending and descending order
numbers = [23, 45, 12, 67, 34]
numbers.sort()
print("Numbers in ascending order:", numbers)
numbers.sort(reverse=True)
print("Numbers in descending order:",numbers)

#5.4 Write a program to merge two dictionaries into one.
dic1={
    "name":"ragini",
    "age":19
}
dic2={
    "class":"be-2nd",
}
dic3=dic1|dic2
print(dic3)


#6.1 Write a program to count the number of vowels in a given string.
Statement = "my name is ragini"
vowels = ["a", "e", "i", "o", "u"]
count = 0
for char in Statement:
    if char in vowels:
        count += 1

print("Number of vowels in the given string is: ", count)


# '''6.2 Write a program to reverse a string and print it.'''
name="ragini"
name=name[::-1]
print(name)

#6.3 Write a program to check if a string is a palindrome'''
name="racecar"
rev=name[::-1]
if rev==name:
    print("palindrome")
else:
    print("no")


#7.1 Write a program to create a text file, write some text into it, and then read and print the content.'''
with open("example.txt", "w") as file:
    file.write("This is a sample text file.")
with open("example.txt", "r") as file:
    print("File content:", file.read())

#7.2 Write a program to append text to an existing file and print the updated content.'''
with open("file.txt","a") as file:
    file.write("this is the appended text")
with open("file.txt","r") as file:
    print(file.read())

#7.3 Write a program to count the number of lines in a text file.
with open("example.txt", "w") as file:
    file.write("hello")
    file.write("\nworld")
    
with open("example.txt", "r") as file:
    print("Number of lines in the file:", len(file.readlines()))

#8.1: Handle division by zero using a try-except block.
try:
    numerator = 8
    denominator = 0
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#8.2: Handle invalid input when the user enters a string instead of a number.
try:
    number = "helo"
    print("You entered:", number)
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

#8.3: Demonstrate the use of finally in exception handling.
try:
    file = open("example.txt", "r")
    print("File content:", file.read())
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Execution of the try-except block is complete.")

#9.1 Write a program to generate 5 random numbers between 1 and 100 and print them.
import random
random_numbers = [random.randint(1, 100) for _ in range(5)]
print("Random Numbers:", random_numbers)

#9.2 Write a program to generate a random number and check if it is prime.
import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

random_number = random.randint(1, 100)
print("Random Number:", random_number)
if is_prime(random_number):
    print("It is a prime number.")
else:
    print("It is not a prime number.")


#9.3 Write a program to simulate rolling a six-sided die.
import random
die_roll = random.randint(1, 6)
print("You rolled a:", die_roll)

#9.4 Write a program to shuffle a list of numbers.
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

#9.5 Write a program to randomly select an item from a list.
import random
items = ['apple', 'banana', 'cherry']
print(random.choice(items))

#9.6 Write a program to generate a random password of given length.
import random
import string

length = 12  

password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

print("Generated Password:", password)

#9.7 Write a program to pick a random card from a standard deck of 52 cards
import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = [rank + ' of ' + suit for suit in suits for rank in ranks]

random_card = random.choice(deck)

print("Random Card:", random_card)

#10.1 Write a program to accept two numbers as command-line arguments, add them, and print the result.
import sys

sys.argv=['sum','5','7']

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

print("Sum:", num1 + num2)

#10.2 Write a program to accept a string as a command-line argument and print its length
import sys

input_string = sys.argv[1]

print("Length of the string:", len(input_string))


#11.1 Write a program to use the math library to calculate the square root of a given number.
import math

number = 4

print("Square root:", math.sqrt(number))

#11.2 Write a program to use the datetime library to print the current date and time.
import datetime

current_datetime = datetime.datetime.now()

print("Current date and time:", current_datetime)

#11.3 Write a program to use the os library to list all files in the current directory
import os

files = os.listdir()

print("Files in the current directory:", files)
