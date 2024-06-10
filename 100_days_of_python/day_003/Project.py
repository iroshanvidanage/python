# author    https://github.com/iroshanvidanage
# date      06/11/2024

import random


def treasure_island():

    print(f'###########################\n'
          f'.Welcome to Treasure Island.\n'
          f'###########################')

    print(f'\nYou\'ll be getting few questions and if you are lucky you\'ll find '
          f'the correct way and win the last price.'
          f'\n\nYour mission is to find the treasure.\n')

    answer = input('Enter the maze: Yes or No (Y/y/N/n)')
    if answer not in 'YyYESYesyes':
        print(f'Need to enter the maze to win the treasure.')
        exit()
        print(f'{answer}')
    path = ['entered']
    answer = input('\nYou have arrived at a T junction can chose to go left or right.'
                   '\nWhich way will you go? Left or Right (L/l/R/r)')
    rand = random.random()
    if answer in 'L/l' and rand > 0.5:
        path.append('left')
    elif answer in 'R/r' and rand >= 0.5:
        path.append('right')
    else:
        game_over()

    answer = input('\nYou have arrived at a door and there is a lake'
                   '\nWhat will you do? Swim or Wait (S/s/W/w)')
    rand = random.random()
    if answer in 'S/s' and rand <= 0.5:
        path.append('swim')
    elif answer in 'W/w' and rand < 0.5:
        path.append('wait')
    else:
        game_over()


def game_over():
    print(f'\nYou have chosen the wrong path'
          f'\nGame Over.'
          f'\n##############################')


treasure_island()
