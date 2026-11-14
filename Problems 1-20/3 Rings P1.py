import random

trials = 10000

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
        #                         else:
        #                             break
        #             else:
        #                 break
        # else:
        #     break
        

print(successful_trials / trials)
    
    
