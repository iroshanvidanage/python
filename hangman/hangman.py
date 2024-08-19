# https://realpython.com/python-hangman/


from random import choice
from draw_hangman import hanged_man


# def user_input():
#     return str(input().strip().lower())
#
#
# def select_random_word():
#     with open("hangman_words.txt", mode="r") as words:
#         words_list = words.readlines()
#
#     return str(choice(words_list).strip().lower())
#
#
# def guess_letter():
#     if user_input() in select_random_word():
#         print(True)
#
#
# print(select_random_word())


# Get Random word guess from words.txt file
def select_random_word():
    with open("words.txt", mode="r") as words:
        words_list = words.readlines()

    return choice(words_list).strip().lower()


# Get user input - loop 6 times or guess correctly
def user_input():
    return input("Guess a letter: ").strip().lower()


# Validate the input length and characters
def validate_user_input(user_input):
    if len(user_input) == 1 and user_input.isalpha():
        return True
    return False


incorrect_guesses = 0
word = [_ for _ in select_random_word()]
print(word)
guessed_word = ["_"] * len(word)

print(hanged_man(0))


while incorrect_guesses < 6:
    player_input = user_input()
    if validate_user_input(player_input):
        if player_input in word:
            guessed_word[word.index(player_input)] = player_input
            # if user input contains a character from guess display it, others as _
            print(" ".join(guessed_word))
            word.remove(player_input)

        else:
            # if user input is incorrect output wrong, display hangman step by step
            incorrect_guesses += 1
            print(incorrect_guesses)
            print(hanged_man(incorrect_guesses))
    else:
        print(f"Invalid input {player_input}")
