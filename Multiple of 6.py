import random
trials = 100000
for i in range(trials):
    while True:
        roll = random.randint(1, 6)
        if roll % 6 == 0:
            break
        else:
            
