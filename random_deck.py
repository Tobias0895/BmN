import numpy as np

def generate_random_deck():
    deck = np.zeros(52)
    # 1 = jack, 2= queen, 3 = king, 4 = ace
    for i in range(deck.size):
        v = np.random.randint(0, 5)

        while np.sum(deck == v) == 4:
            v = np.random.randint(0, 5)
        deck[i] = v
    np.random.shuffle(deck)
    deck = np.vstack((deck[:26], deck[26:]))
    return deck