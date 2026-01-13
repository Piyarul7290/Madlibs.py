import random

def play():
    user = input("what is your choice? 'r' Enter your choice (rock, paper, scissors): ")
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You win!'
    
    return 'You lose!'
    
    def is_win(player, opponent):
        if (player == 'rock' and opponent == 'scissors') or \
              (player == 'scissors' and opponent == 'paper') or \
                (player == 'paper' and opponent == 'rock'):
            return True
        return False
    