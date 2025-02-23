import unittest

class TestExample(unittest.TestCase):
    def test_is_number(self):
        self.assertTrue(int('10') == 10)
    def test_not_number(self):
        with self.assertRaises(ValueError):
            int('no')

if __name__ == '__main__':
    # unittest.main()
    unittest.main(verbosity=2, failtest=True) # similar to `python3 test_assertion.py -v -f`