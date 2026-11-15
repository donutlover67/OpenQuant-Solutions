"""Now you shoot 3n arrows. Derive an expression that represents the 
probability that you land exactly n arrows in each of the 3 rings?"""

import numpy as np

n = int(input("Enter the value of n: "))

trials = 100000
successful_trials = 0

def shot():
    result = np.random.choice([1, 2, 3], p=[1/9, 3/9, 5/9])
    return result

for i in range(trials):
    rings = []
    for j in range(3 * n):
        shot_result = int(shot())
        rings += [shot_result]

    if rings.count(1) == n and rings.count(2) == n and rings.count(3) == n:
        successful_trials += 1
print(successful_trials / trials)







# successful_trials = 0
# for i in range(trials):
#     rings = []
#     for j in range(3):
#         rings  += [random.randint(1, 9)]

#     # print(rings)

#     for i in range(len(rings)):
#         if rings[i] == 1:
#             # print("Ring 1 is present")
#             True

#             if True:
#                 for i in range(len(rings)):
#                     if 1 < rings[i] < 5:
#                         # print("Ring 2 is present")
#                         True
#                         if True:
#                             for i in range(len(rings)):
#                                 if rings[i] >= 5:
#                                     # print("Ring 3 is present")
#                                     True
#                                     successful_trials += 1

        

# print(successful_trials / trials)