import random

# create a random number for the player to guess.
answer = random.randint(1, 10)

def inform(guess: chr):
    if guess == '=':
        print(f'{"you win":=^80}')
    elif guess == '-':
        print(f'{"higher":+^80}')
    elif guess == '+':
        print(f'{"lower":-^80}')
    else:
        raise ValueError(f'Unknown guess type')

def play():
    # Prompt for a guess between 1 and 10 convert the value to an int.
    # this app will fail if a non-numeric guess is entered.
    while (guess := int(input('guess a number between 1 and 10> '))) != answer:
        if guess > answer:
            inform('+')
        elif guess < answer:
            inform('-')
    else:
        inform('=')

if __name__ == '__main__':
    play()
