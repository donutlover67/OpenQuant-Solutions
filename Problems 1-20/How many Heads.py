"""There are three coins in a hat. One with probability 1/3 of getting heads, 
another with probability 2/3 of heads, and the last coin always landing on 
heads. I take one out and flip it twice landing on heads both times. If I flip 
the coin twelve more times, how many heads do you expect among these flips?"""

import numpy as np
import random

def draw():
    result = np.random.choice([1, 2, 3], p = [1/3, 1/3, 1/3])
    return result

trials = 100000
Draw = []
success = []



for i in range(trials):
    coin = draw()
    if coin == 1:
        Draw = []
        for j in range(14):
            Draw += [int(np.random.choice([0, 1], p = [2/3, 1/3]))]
        if Draw[0] == 1 and Draw[1] == 1:
            success.append(Draw.count(1) - 2)


    elif coin == 2:
        Draw = []
        for j in range(14):
            Draw += [np.random.choice([0, 1], p = [1/3, 2/3])]
        if Draw[0] == 1 and Draw[1] == 1:
            success.append(Draw.count(1) - 2)

            
    elif coin == 3:
        Draw = []
        for j in range(14):
            Draw += [np.random.choice([0, 1], p = [0, 1])]
        if Draw[0] == 1 and Draw[1] == 1:
            success.append(Draw.count(1) - 2)


print(sum(success) / len(success))
