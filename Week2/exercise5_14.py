# Find the smallest n such that n^2 > 12,000
# Author: Brian Hamburg

#define variables
n = 0
result = 0

# loop!
while result <= 12000:
    result = n ** 2
    n += 1

# print result
print("n = " + str(n - 1))
