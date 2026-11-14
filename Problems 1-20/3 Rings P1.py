"""You are shooting arrows at a target with three rings: there is a circle with 
a 4 inch radius, a ring around it with an 8 inch radius, and a ring around that 
with a 12 inch radius. Each arrow hits the target somewhere uniformly at random.

What’s the probability that you land exactly one arrow in each of the 
three rings?"""

import random

trials = 100000

ring = 0
successful_trials = 0
for i in range(trials):
    rings = []
    for j in range(3):
        rings  += [random.randint(1, 9)]

    # print(rings)

    for i in range(len(rings)):
        if rings[i] == 1:
            # print("Ring 1 is present")
            True

            if True:
                for i in range(len(rings)):
                    if 1 < rings[i] < 5:
                        # print("Ring 2 is present")
                        True
                        if True:
                            for i in range(len(rings)):
                                if rings[i] >= 5:
                                    # print("Ring 3 is present")
                                    True
                                    successful_trials += 1

        

print(successful_trials / trials)
    
    
