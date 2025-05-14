import random_deck
from player import Player
        
class Game:
    def __init__(self, name1='Alice', name2='Bob'):
        self.deck = random_deck.generate_random_deck()
        self.player1 = Player(starting_hand=self.deck[0], name=name1)
        self.player2 = Player(starting_hand=self.deck[1], name=name2)
        self.pile = []
        self.trive_count = 0
        self.current_player = self.player1

    def update_turn(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1


    def play_game(self):
        while self.player1.hand.size and self.player2.hand.size:
            card = self.current_player.play_card()
            if card is None:
                break
            self.pile.append(card)
            self.update_turn()
            if self.pile[-1] == 0:
                continue
            else:
                self.play_trife(self.current_player, self.pile[-1])
                self.update_turn()
                self.current_player.add_cards(self.pile)
                self.pile = []

        winner = self.player1 if self.player1.hand.size else self.player2
        cards_played = self.player1.cards_played_count + self.player2.cards_played_count
        print(f'Game ended; winner is {winner.name}')
        print(f'Cards played {cards_played}')
        return winner, cards_played


    def play_trife(self, player, card_value):
        self.trive_count +=1
        trive = False
        for _ in range(int(card_value)):
            card2 = player.play_card()
            if card2 is None:
                return False # out of cards
            self.pile.append(card2)
            if card2 != 0:
                trive = True
                break
            else:
                continue

        if trive:
            self.update_turn()
            trive = self.play_trife(self.current_player, self.pile[-1])
        return trive

if __name__ == '__main__':
    print("Starting the game...")
    Game = Game()
    Game.play_game()