# Twin primes
# Author: Brian Hamburg

def main():
    i = 2
    while i <= 1000:
        twin = i + 2
        if isPrime(i) and isPrime(twin):
            print("(", end = "")
            print(i, end = "")
            print(", ", end = "")
            print(twin, end = "")
            print(")", end = "")
            print()
        i += 1

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

main()
