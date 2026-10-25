"""You roll a fair six-sided and sum the outcomes until you reach a multiple of 6. 
What is the expected number of times you expect to roll the die.
"""

import random
trials = 100000
for i in range(trials):
    while True:
        roll = random.randint(1, 6)
        if roll % 6 == 0:
            break
        else:
            
