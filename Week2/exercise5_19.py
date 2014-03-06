# Display a pyramid
# Author: Brian Hamburg

n = eval(input("Enter the number of lines: "))

for i in range(1, n + 1):
    
    # Print leading spaces
    for j in range(n - i, 0, -1):
        print("  ", end = "")
        
    # print numbers
    for j in range(i, 0, -1):
        print(j, end = " ")
    for j in range(1, i, +1):
        print(j + 1, end = " ")

    # print trailing spaces
    for j in range(n - i, 0, -1):
        print("  ", end = "")
    
    print()
