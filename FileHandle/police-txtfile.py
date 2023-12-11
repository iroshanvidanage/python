import re
hand = open('police.txt')
h_file = open('police-func.txt', 'w')
for line in hand:
    line = line.rstrip()
    if re.findall('Director', line):
        y = re.findall('>(Director.+?)<', line)
        print(y[0])
        h_file.write(y[0] + '\n')

h_file.close()
hand.close()