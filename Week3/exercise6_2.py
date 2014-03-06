# Sum the digits in an integer
# Author: Brian Hamburg

def main():
    number = eval(input("Enter a number and I will sum its digits: "))

    print("The sum of your digits is",sumDigits(number))

def sumDigits(n):
    currentSum = 0
    while n != 0:
        currentSum = currentSum + (n % 10)
        n = n // 10
        
    return currentSum

main()
