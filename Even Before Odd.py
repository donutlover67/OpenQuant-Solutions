"""
Suppose you roll a fair 6-sided die until you've seen all 6 faces. 
What is the probability you won't see an odd numbered face until you have seen all even numbered faces?
"""

import random

roll_dice = lambda: random.randint(1, 6)

seen_faces = set()
winning_trials = 0
total_trials = 100000

for i in range(total_trials):
    seen_faces.clear()
    while(True):
        roll = roll_dice()
        seen_faces.add(roll)
        if roll % 2 == 1 and len(seen_faces) < 4:
            break
        if len(seen_faces) == 6:
            winning_trials += 1
            break
print(winning_trials / total_trials)