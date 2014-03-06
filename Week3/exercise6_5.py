# Sort three numbers
# Author: Brian Hamburg

def main():
    # get numbers from user
    num1, num2, num3 = eval(input("Enter three numbers: "))

    # run function
    displaySortedNumbers(num1, num2, num3)

def displaySortedNumbers(a, b, c):
    if a < b:
        if a < c:
            if b < c:
                print("The sorted numbers are", a, b, c)
            else: print("The sorted numbers are", a, c, b)
        else: print("The sorted numbers are", c, a, b)
    else:
        if b < c:
            if a < c:
                print("The sorted numbers are", b, a, c)
            else: print("The sorted numbers are", b, c, a)
        else:
            print("The sorted numbers are", c, b, a)

main()
