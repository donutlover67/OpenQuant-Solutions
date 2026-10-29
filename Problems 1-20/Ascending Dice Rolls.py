"""You throw three fair dice consecutively. What is the probability that you obtain 
three numbers in strictly increasing order?
"""

import random

trials = 10000
good = 0
for i in range(trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    if dice1 < dice2 < dice3:
        good += 1
print(good/trials)

