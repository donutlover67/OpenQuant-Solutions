import random

trials = 10000
success = 0

def deck():
        cards = []
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["H", "D", "C", "S"]
        for suit in suits:
            for value in values:
                cards.append([suit, value])
        return cards


for i in range(trials):
    Deck = deck()
    picks = []


    for j in range(5):
        pick = random.randint(0, len(Deck) - 1)
        picked_card = Deck[pick]
        Deck.pop(pick)
        picks.append(picked_card)

    picks1 = []

    for item in picks:
        picks1 += [item[1]]

    picks2 = list(set(picks1))
    if len(picks2) == 2:
        print(f"Sorted picks: {picks2}")

    if len(picks2) == 2:
        if picks.count(pick) == 4 or picks.count(pick) == 1:
            success += 1
print(success / trials)
# I will sort the picks list and if theres only 2 unique values in the list
# and I know theres only one of them thats different, there has to be 4 of a kind.