# Compute the perimeter of a triangle
# Author: Brian Hamburg

# prompt the student
edgeA, edgeB, edgeC = eval(input("Enter three edges: "))

# check validity and print results
if edgeA + edgeB > edgeC and edgeB + edgeC > edgeA and edgeC + edgeA > edgeB:
    print("The perimeter is", edgeA + edgeB + edgeC)
else:
    print("The input is invalid.")
