# Palindromic prime
# Author: Brian Hamburg

def main():
    counter = 1
    i = 2 
    while counter <= 100:
        if isPrime(i) and isPalindrome(i):
            print(i, end = " ")
            if counter % 10 == 0:
                print()
            counter += 1
        i += 1

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

def isPalindrome(number):
    return number == reverse(number)

def reverse(number):
    result = 0
    while number != 0:
        remainder = number % 10
        result = result * 10 + remainder
        number = number // 10

    return result

main()
