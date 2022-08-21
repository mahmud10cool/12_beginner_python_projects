import random

def play():
    print('Welcome to the rock paper scissors game! \n')
    user = input("Your choice: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print('Computer choice: ', computer)
        return 'tie'

    if is_win(user, computer):
        print('Computer choice: ', computer)
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())