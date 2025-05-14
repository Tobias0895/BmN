import numpy as np

class Player:
    def __init__(self, starting_hand=None, name=None):
        self.name = name
        self.hand = starting_hand
        self.starting_hand = starting_hand
        self.cards_played = []
        self.cards_played_count = 0

    def add_cards(self, cards):
        self.hand = np.append(self.hand, cards)

    def play_card(self):
        if self.hand.size:
            played_card = self.hand[0]
            self.hand = self.hand[1:]
            self.cards_played_count += 1
            self.cards_played.append(played_card)
            return played_card