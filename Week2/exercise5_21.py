# Display another pyramid
# Author: Brian Hamburg

for i in range(1, 9):
    
    # Print leading spaces
    for j in range(8 - i, 0, -1):
        print("    ", end = "")
        
    # print numbers
    k = 1
    for j in range(0, i):
        print(format(k, ">3d"), end = " ")
        k += k
    k = int(k / 2)
    for j in range(i, 1, -1):
        k = int(k / 2)
        print(format(k, ">3d"), end = " ")

    # print trailing spaces
    for j in range(8 - i, 0, -1):
        print("    ", end = "")
    
    print()
