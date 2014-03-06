# Simulation: heads or tails
# Author: Brian Hamburg

import random

# define counter variables
heads = 0
tails = 0

# start loop for 1 million flips
for i in range(1000000):

    # get random flip variable
    flip = random.randint(0, 1)

    # test flip and assign to tally
    if flip == 0:
        heads += 1
    else:
        tails += 1

# print results
print("Number of heads:", heads)
print("Number of tails:", tails)
