# author    https://github.com/iroshanvidanage
# date      05/13/2023

# 1. Create a greeting for your project.

def greetings():
    print('''
Welcome to the Band name generator.
    ''')


# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine two strings and print the band name.
# 5. Make sure the input cursor shows on a new line.


def user_city_pet():
    city = str(input('What is the city you grew in?\n'))
    pet = str(input('What is the name of your pet?\n'))
    return 'Your band name could be ' + city + ' ' + pet


greetings()  # execution
print(user_city_pet())