"""You have a basket with an assortment of fruits. Inside this basket, there are 
10 apples, 20 oranges, and 30 peaches. You take out fruits one by one and at 
random. What is the probability that there will be at least 1 orange and 1
peach in the basket after you've taken out all the apples?"""

import random

basket = ["apple"] * 10 + ["orange"] * 20 + ["peach"] * 30
successful_trials = 0
trials = 100000

for i in range(trials):
    basket = ["apple"] * 10 + ["orange"] * 20 + ["peach"] * 30
    while basket.count("apple") > 0:
        basket.pop(random.randrange(len(basket)))
    if basket.count("apple") == 0 and basket.count("orange") > 0 and basket.count("peach") > 0:
        successful_trials += 1

print(successful_trials / trials)



# for i in range(trials):
#     while len(basket) > 0:
#         basket.pop(random.randrange(len(basket)))
        