import random
import os

def read_player_highest_score(player_name):
    if os.path.exists(player_name + '.txt'):
        with open(player_name + '.txt', 'r') as file:
            return int(file.read().strip())
    else:
        return 0

def update_player_highest_score(player_name, score):
    with open(player_name + '.txt', 'w') as file:
        file.write(str(score))

def get_round_winner(player_move, computer_move):
    if player_move == computer_move:
        return 'draw'
    elif (player_move == 'rock' and computer_move == 'scissors') or \
         (player_move == 'paper' and computer_move == 'rock') or \
         (player_move == 'scissors' and computer_move == 'paper'):
        return 'player'
    else:
        return 'computer'

def play_rock_paper_scissors():
    print('Welcome to Rock Paper Scissors!')
    player_name = input('Enter your name: ')
    player_highest_score = read_player_highest_score(player_name)
    print(f'Your highest score is {player_highest_score}')

    while True:
        print('Choose your move: (rock, paper, scissors)')
        player_move = input().lower()
        while player_move not in ['rock', 'paper', 'scissors']:
            print('Invalid choice. Please enter rock, paper, or scissors.')
            player_move = input().lower()

        computer_move = random.choice(['rock', 'paper', 'scissors'])
        print(f'Computer chooses {computer_move}.')

        round_winner = get_round_winner(player_move, computer_move)
        if round_winner == 'player':
            print('You win!')
            player_highest_score += 1
            update_player_highest_score(player_name, player_highest_score)
        elif round_winner == 'computer':
            print('Computer wins!')
        else:
            print('It\'s a draw!')

        print(f'Your current score is {player_highest_score}.')
        play_again = input('Do you want to play again? (y/n)').lower()
        if play_again != 'y':
            print('Thanks for playing!')
            break

if __name__ == '__main__':
    play_rock_paper_scissors()
