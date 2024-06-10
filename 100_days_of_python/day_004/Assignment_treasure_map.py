# author    https://github.com/iroshanvidanage
# date      06/10/2024


import random


line1 = ["\N{upside-down face}", "\N{upside-down face}", "\N{upside-down face}"]
line2 = ["\N{upside-down face}", "\N{upside-down face}", "\N{upside-down face}"]
line3 = ["\N{upside-down face}", "\N{upside-down face}", "\N{upside-down face}"]
map1 = [line1, line2, line3]

position = input("Enter the position: ").lower()

map1[ord(position[0])-97][int(position[1])-1] = "X"
print(f"{line1}\n{line2}\n{line3}")
