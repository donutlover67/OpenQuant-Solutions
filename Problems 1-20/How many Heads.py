"""There are three coins in a hat. One with probability 1/3 of getting heads, 
another with probability 2/3 of heads, and the last coin always landing on 
heads. I take one out and flip it twice landing on heads both times. If I flip 
the coin twelve more times, how many heads do you expect among these flips?"""

import numpy as np
import random

def draw():
    result = np.random.choice([1, 2, 3], p = [1/3, 1/3, 1/3])
    return result

trials = 10000
draw1 = []
draw2 = []
draw3 = []
success1 = 0
success2 = 0
success3 = 0

for i in range(trials):
    coin = draw()
    if coin == 1:
        for j in range(14):
            draw1 += [np.random.choice([0, 1], p = [2/3, 1/3])]
        if draw1[0] == 1 and draw1[1] == 1:
            success1 += 1
    elif coin == 2:
        for j in range(14):
            draw2 += [np.random.choice([0, 1], p = [1/3, 2/3])]
        if draw2[0] == 1 and draw2[1] == 1:
            success2 += 1
    elif coin == 3:
        for j in range(14):
            draw3 += [np.random.choice([0, 1], p = [0, 1])]
        if draw3[0] == 1 and draw3[1] == 1:
            success3 += 1

if coin == 1:
    print(success1 / trials)
elif coin == 2:
    print(success2 / trials)
else:
    print(success3 / trials)