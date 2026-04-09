import random
Secret_number = random.randint(1,10)
Guess = int(input('Guess the number(between 1 and 10): '))
while Guess!=Secret_number:
    print("Oops! That's the wrong number, Guess again.")
    Guess = int(input('Guess again: '))

print('You guessed the number')
input('Press space to exit')