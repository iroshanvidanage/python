# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
# represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any
# letters.


# noinspection PyGlobalUndefined
class Solution:
    def letter_combination(self, digits):
        string_map = {
            "2": ["abc"],
            "3": ["def"],
            "4": ["ghi"],
            "5": ["jkl"],
            "6": ["mno"],
            "7": ["pqrs"],
            "8": ["tuv"],
            "9": ["wxyz"]
        }
        if len(digits) == 1:
            return string_map[digits]
        elif len(digits) == 0:
            return []
        else:
            a = digits[0]
            for ch in string_map[a]:
                return [ch + x for x in Solution.letter_combination(digits[1:])]


key_digits = ['23456789']
digits = input('Digits: ')


# for _ in digits:
#     if _ not in key_digits:
#         print("Digits should be between 2-9")
#     else:
#         combine = Solution.letter_combination(digits)
#         print(combine)

def letter_combination(digit_input):
    string_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    if len(digit_input) == 1:
        return string_map[digit_input]
    elif len(digit_input) == 0:
        return []
    else:
        a = digit_input[0]
        temp_res = []
        for ch in string_map[a]:
            temp_res.append([ch + x for x in letter_combination(digit_input[1:])])
        return temp_res


combine = letter_combination(digits)
print(combine)

# Answer


"""
    def letter_combinations(digits):
        if digits == "":
            return []

        string_maps = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


    result = [""]

    for number in digits:
        temp = []
        for mn in result:
            for char in string_maps[number]:
                temp.append(mn + char)
        result = temp
    return result
"""
