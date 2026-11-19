"""Independent thought process of using monte carlo to find out if its a higher
probability to get at least a pair or getting 5 unique cards from drawing five"""

import random

def deck():
    Cards = []
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["H", "D", "C", "S"]
    for suit in suits:
        for value in values:
            Cards.append([suit, value])
    return Cards

trials = 200000
success2 = 0
success5 = 0

for i in range(trials):

    cards = deck()
    drawn_cards = []
    unique_cards = []

    for j in range(5):
        drawn_index = random.randint(0, len(cards) - 1)
        drawn_card = cards[drawn_index]
        cards.pop(drawn_index)
        drawn_cards.append(drawn_card)

    for item in drawn_cards:
        unique_cards += [item[1]]

    unique_cards = list(set(unique_cards))
    if len(unique_cards) == 4:
        success2 += 1
    elif len(unique_cards) == 5:
        success5 += 1

if success2 > success5:
    print("singular pair more common than getting 5 distinct cards")
elif success5:
    print("5 distinct more common than one pair")


