# Display leap years
# Author: Brian Hamburg

# define line counter
j = 0

# define range of years
for i in range(2001, 2101):
    
    # print and add 1 to line counter (j) if leap year
    if i % 4 == 0:
        print(str(i), end = " ")
        j += 1
    # if end of line, print return and reset line counter
    if j > 9:
        print()
        j = 0
