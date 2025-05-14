from typing import Type
import game
import os
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Hold a Beggar my neighbor competition')
parser.add_argument('-con', '--contestants', type=str, help='File containing the contestants')
parser.add_argument('-t', '--tie-breaker', type=bool, help='If the game should be repeated to break all the ties', default=False)
args = parser.parse_args()

try:
    cf= open(args.contestants, 'r')
    contestent_list = np.char.array(cf.readlines()).replace('\n', '')
    cf.close()
except TypeError:
    contestent_list = ['Kristian', 'Xavier', 'Dhwanil', 'Kelly', 'Paul', 'Luna', 'Dion', 'Puck', 'Yannick', 'Eirini', 'Francesco', 'Sam', 'Suzanne', 'Tobias']

win_counts = np.zeros(len(contestent_list))
for i in range(len(contestent_list)):
    for j in range(i + 1, len(contestent_list)):
        c1 = contestent_list[i]
        c2 = contestent_list[j]
        c1_file = f'{os.getcwd()}/results/{c1}-results.txt'
        c2_file = f'{os.getcwd()}/results/{c2}-results.txt'

        f1 = open(c1_file, '+a')
        f2 = open(c2_file, '+a')
        if os.path.getsize(c1_file) == 0:
            f1.write(f'Welcome {c1}! These are the results from your participation in the Astrothings Beggar-your-neighbor tournament!\n \n')

        if os.path.getsize(c2_file) == 0:
            f2.write(f'Welcome {c2}! These are the results from your participation in the Astrothings Beggar-your-neighbor tournament!\n\n')



        g = game.Game(c1, c2)
        winner, cards_played = g.play_game()
        f1.write(f'In your match against {c2}, {winner.name} won the game! \n Your starting hand: {g.player1.starting_hand} \n {c2} starting hand {g.player2.starting_hand} \n You played first\n\n') 
        f2.write(f'In your match against {c1}, {winner.name} won the game! \n Your starting hand: {g.player2.starting_hand} \n {c2} starting hand {g.player1.starting_hand} \n {c1} played first\n\n')
        if winner.name == c1:
            win_counts[i] += 1
        else:
            win_counts[j] += 1


zipped = zip(win_counts, contestent_list)
wins, participants = zip(*sorted(zipped, key=lambda x: -x[0]))
wins = np.array(wins)
if args.tie_breaker:
    while np.unique(wins).size != len(wins):
        for i, (score, contestent) in enumerate(zip(wins, participants)):
            for j in range(i + 1, len(wins)):
                if wins[j] == score: # There is a tie
                    g = game.Game(c1, c2)
                    winner, cards_played = g.play_game()
                    if winner.name == contestent:
                        wins[i] += 1
                    else:
                        wins[j] += 1
                    score = wins[i]
                    if wins[i-1] == score: # previous tie breaker has tied you again with the previous contestant
                        g = game.Game(c1, c2)
                        winner, cards_played = g.play_game()
                        if winner.name == contestent:
                            wins[i] += 1
                        else:
                            wins[i-1] += 1
        


    zipped = zip(wins, contestent_list)
    wins, participants = zip(*sorted(zipped, key=lambda x: -x[0]))
print('Total games played:', np.sum(wins))
for i, (score, contestent) in enumerate(zip(wins, participants)):
    score_file = f'{os.getcwd()}/results/End_scores.txt' 
    with open(score_file, '+a') as sf:
        sf.write(f'{i + 1}. {contestent} With {score} wins! \n')
