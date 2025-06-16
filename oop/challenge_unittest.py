# Python Unittest - Assertions

import unittest

class InvalidOperation(Exception): ...

def simple_calculator(a, b, op):
    operators = {
        '+' : a + b,
        '-' : a - b,
        '*' : a * b,
        '/' : a / b,
        '%' : a % b,
        '//' : a // b
    }
    try:
        return operators[op]
    except : # since the key is not defined the error will be KeyError
        raise InvalidOperation(f'{op} is not a valid operation.....')

class TestChallenge1(unittest.TestCase):
    def test_operations(self):
        input_output: list[tuple[tuple[int, int, str], int]] = [
            ((1, 1, '+'), 2),
            ((1, 1, '-'), 0),
            ((1, 8, '*'), 8),
            ((8, 2, '/'), 4),
            ((5, 2, '%'), 1),
            ((5, 2, '//'), 2)
        ]

        ###################################################################################
        #
        # Assignments: 
        # 
        # Ensure all existing operators defined in the simple_calculator function
        # return the expected results.
        #
        # input_output : ((args), output)
        #
        #
        # 1). For each input/output pair in the above list: provide the the arguments and assert
        # the values are equal to the given value.
        #
        ###################################################################################
        for each_in, each_out in input_output:
            self.assertEqual(simple_calculator(each_in[0], each_in[1], each_in[2]), each_out)


    def test_unknown_operation(self):
        input_side_effect: list[tuple[tuple[int, int, str], int]] = [
            ((1, 1, '&'), InvalidOperation),
            ((1, 1, '^'), InvalidOperation),
            ((1, 8, '@'), InvalidOperation)
        ]

        ###################################################################################
        #
        # Assignments: 
        # 
        # Ensure undefined operators raise exceptions.
        # 
        # 1). For each input/side_effect pain in the above list: assert that 
        # InvalidOperation is raise.
        #
        ###################################################################################
        for each_in, each_exception in input_side_effect:
            self.assertRaises(each_exception, simple_calculator, each_in[0], each_in[1], each_in[2])
        

if __name__ == '__main__':
    print(unittest.main(verbosity=1, failfast=True))