def compare(str_1, str_2):
    count = 0

    if len(str_1) > len(str_2):
        return -1

    for i in range(len(str_1)):
        # print(str_1[i], str_2[i], i)
        if len(str_1) > len(str_2):
            return -2
        elif str_1[i] != str_2[i] and (i+1) < len(str_2):
            if str_1[i] == str_2[i + 1]:
                str_2 = str_2[:i] + str_2[i + 1:]
                # print(str_2)
                count += 1
            else:
                return -1
        elif str_1[i] != str_2[i]:
            return -3

    if len(str_1) < len(str_2):
        count += (len(str_2) - len(str_1))
        return count
    elif len(str_1) == len(str_2):
        return count
    else:
        return -4


answer = []

for _ in range(int(input())):
    str1 = str(input())
    str2 = str(input())

    answer.append(compare(str_1=str1, str_2=str2))

# print(answer)

for _ in range(len(answer)):
    if answer[_] < 0:
        print('Case #' + str(_+1) + ': ' + 'IMPOSSIBLE')
    else:
        print('Case #' + str(_ + 1) + ': ' + str(answer[_]))
