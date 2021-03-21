import random

class Deal_Card:

    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def deal_one_card(self):
        new_card = random.choice(self.cards)
        return new_card
    
    def deal_two_card(self, hand):
        hand.append(random.choice(self.cards))
        hand.append(random.choice(self.cards))
        return hand



