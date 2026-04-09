import random
def RPS():
    Ask = input("Rock..Paper..Scissors..Shoot!(Your choice) ").strip().lower()
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    print(f'Computer choses,{computer}')
    if Ask == computer:
        print('Oops! A tie!!')
    elif Ask not in choices:
        print('Invalid Input!')
    elif (Ask == 'rock' and computer == 'scissors') or (Ask == 'scissors' and computer == 'paper') or (Ask == 'paper' and computer == 'rock'):
        print('You win!')
    else:
        print('Computer wins!')

def main():
    while True:
        RPS()
        ask_again = input('Would you like to play again?(Y/N) ').strip().lower()
        if ask_again != 'y':
            break

main()