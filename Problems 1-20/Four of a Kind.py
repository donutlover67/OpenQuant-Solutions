import random

trials = 10000
success = 0

def deck():
        cards = []
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["H", "D", "C", "S"]
        for suit in suits:
            for value in values:
                cards.append([(suit, value)])
        return cards
    


for i in range(trials):
    deck = deck()
    for j in range(5):
        pick = random.randint(len(deck))
        picks += pick
    if picks[0][1] == picks[1][1] == picks[2][1] == picks[3][1]:
        success += 1
print(success / trials)