"""You roll a fair six-sided and sum the outcomes until you reach a multiple of 6. 
What is the expected number of times you expect to roll the die.
"""

import random
trials = 100000
count  = 0
for i in range(trials):
    roll = random.randint(1, 6)
    count += 1
    while True:
        if roll % 6 == 0:
            break
        else:
            roll += random.randint(1, 6)
            count += 1
            continue
print(count / trials)
