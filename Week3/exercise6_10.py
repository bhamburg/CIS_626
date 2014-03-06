# Use the isPrime Function
# Author: Brian Hamburg

def main():
    # set counter to zero
    counter = 0
    for x in range(2, 10000):
        if isPrime(x):
            counter += 1

    print("There are",counter,"prime numbers less than",10000)

# Check whether number is prime 
def isPrime(number):
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0: # If true, number is not prime
            return False # number is not a prime

    return True # number is prime

main()
