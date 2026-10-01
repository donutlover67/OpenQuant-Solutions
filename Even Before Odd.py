"""
Suppose you roll a fair 6-sided die until you've seen all 6 faces. 
What is the probability you won't see an odd numbered face until you have seen all even numbered faces?
"""

import random
winning_trials = 0
trials = 100000
dice_batch = [1] * 3 + [0] * 3
for i in range(trials):
    random.shuffle(dice_batch)
    if dice_batch[3:]== [1, 1, 1]:
        winning_trials += 1
print(winning_trials / trials)
