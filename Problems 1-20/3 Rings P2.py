"""Now you shoot 3n arrows. Derive an expression that represents the 
probability that you land exactly n arrows in each of the 3 rings?"""

import numpy as np

n = int(input("Enter the value of n: "))

trials = 100000
successful_trials = 0

for i in range(trials):
    rings = []
    for j in range(3 * n):
        shot_result = np.random.choice([1, 2, 3], p=[1/9, 3/9, 5/9])
        rings += [shot_result]

    if rings.count(1) == n and rings.count(2) == n and rings.count(3) == n:
        successful_trials += 1
print(successful_trials / trials)
