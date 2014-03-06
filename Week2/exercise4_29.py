# Geometry: two circles
# Author: Brian Hamburg

# prompt the student
x1, y1, r1 = eval(input("Enter circle one's center x- and y-coordinates and radius: "))
x2, y2, r2 = eval(input("Enter circle two's center x- and y-coordinates and radius: "))

# check the distance between center points
distanceBetweenCenters = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

# test and print
if distanceBetweenCenters <= abs(r1 - r2):
    print("Circle two is inside circle one.")
elif distanceBetweenCenters <= abs(r2 - r1):
    print("Circle one is inside circle two.")
elif distanceBetweenCenters <= r1 + r2:
    print("Circle two overlaps circle one.")
else:
    print("Circle two does not overlap circle one.")
