"""There are three coins in a hat. One with probability 1/3 of getting heads, 
another with probability 2/3 of heads, and the last coin always landing on 
heads. I take one out and flip it twice landing on heads both times. If I flip 
the coin twelve more times, how many heads do you expect among these flips?"""

import numpy as np

def draw():
    result = np.random.choice([1, 2, 3], p = [1/3, 2/3, 1])
    print(result)
draw()