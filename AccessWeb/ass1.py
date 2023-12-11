import re

#text = open('sample-data-ass1.txt')
text = open('actual-data-ass1.txt')

num_list = list()
for line in text:
    line = line.rstrip()
    numbers = re.findall('[0-9]+',line)
    #print(numbers)
    if len(numbers) != 0:
        for _ in numbers:
            num_list.append(int(_))

print(sum(num_list))
