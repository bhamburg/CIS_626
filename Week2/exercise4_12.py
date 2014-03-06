# Check a number
# Author: Brian Hamburg

# prompt the student
answer = eval(input("Enter an integer: "))

# test for remainders
test5 = answer % 5 == 0
test6 = answer % 6 == 0

# results
print("Is", answer, "divisible by 5 and 6?", test5 + test6 == 2)
print("Is", answer, "divisible by 5 or 6?", test5 + test6 > 0)
print("Is", answer, "divisible by 5 or 6, but not both?", test5 + test6 == 1)
