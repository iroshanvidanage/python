# author    https://github.com/iroshanvidanage
# date      05/13/2023

def calculate_string(user_string):
    # without in built methods
    num = 0
    for _ in user_string:
        num += 1

    return num


u_string = str(input('Enter_user_name: '))
print(calculate_string(u_string))
print(len(u_string))



####################################################

# author    https://github.com/iroshanvidanage
# date      05/13/2023

def switch_values(a, b):

    a, b = b, a
    return a, b


value_1 = input('Input value 1: ')
value_2 = input('Input value 2: ')
[value_1, value_2] = switch_values(value_1, value_2)

print('Value 1 ', value_1, '.\nValue 2 ', value_2, '.')