# Geometry: area of a pentagon
import math
s = eval(input("Enter the side: "))
area = (5 * (s ** 2)) / (4 * math.tan(math.pi / 5))
print("The area of the pentagon is", area)