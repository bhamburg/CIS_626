# Game: multiplication quiz
# Author: Brian Hamburg

import random

# generate random numbers
number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

# prompt the student
answer = eval(input("What is " + str(number1) + " x " + str(number2) + "? "))

if number1 * number2 == answer:
    print("You are correct!")
else:
    print("Your answer is wrong.\n", number1, "x", number2, "=", number1 * number2)
