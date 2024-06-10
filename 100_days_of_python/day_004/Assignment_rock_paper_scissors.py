# author    https://github.com/iroshanvidanage
# date      06/10/2024


import random


choices = ["\N{rock}", "\N{scroll}", "\N{axe}"]
print(choices)
user_choice = int(input())-1
user_emoji = choices[user_choice]
random.shuffle(choices)
computer_emoji = choices[random.randint(0, 2)]
if user_emoji == computer_emoji:
    print(f"{user_emoji} == {computer_emoji}")
else:
    print(f"{user_emoji} =! {computer_emoji}")
