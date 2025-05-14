import game
import os
import numpy as np
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
sort_by_wins = sorted(zipped, key=lambda x: -x[0])

for i, (score, contestent) in enumerate(sort_by_wins):
    score_file = f'{os.getcwd()}/results/End_scores.txt' 

    with open(score_file, '+a') as sf:
        sf.write(f'{i + 1}. {contestent} With {score} wins! \n')
