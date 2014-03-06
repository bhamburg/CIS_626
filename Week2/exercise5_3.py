# Conversion from kilos to pounds
# Author: Brian Hamburg

# set kg counter
kg = 1

# print table labels
print("Kilograms    Pounds")

# print table
while kg < 200:
    print(format(kg, "<3d"), format(kg * 2.2, "15.1f"))
    kg += 2
