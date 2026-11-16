"""Suppose you roll three fair 100-sided die. What is the expected value 
of the lowest roll?"""

import random

trials = 1000000
minimums = []

def roll():
    return random.randint(1, 100)

for i in range(trials):
    rolls = [roll(), roll(), roll()]
    minimums.append(min(rolls))

print(sum(minimums) / len(minimums))
