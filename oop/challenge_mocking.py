# Python Unittest - Mocking

import json, unittest
from unittest.mock import MagicMock
from urllib.request import urlopen

def get_json(url, getter_callable=urlopen):
    with getter_callable(url) as f:
        return json.loads(f.read())
    

class TestChallenge2(unittest.TestCase):
    '''
    `mock_response.read.retrun_value` must return bytes, hence the `.encode('utf-8')`.
    `mock_urlopen.return_value.__enter__.return_value` mocks the context manager behavior of `urlopen`.
    '''

    def test_get_json(self):
        expect = {
            "sun" : 80,
            "mon" : 86,
            "tue" : 92,
            "wed" : 76,
            "thu" : 79,
            "fri" : 91,
            "sat" : 87,
        }
        test_url = 'test://url.example.domain/weather'

        ###################################################################################
        #
        # Assignments: 
        # 
        # Ensure the get_json function returns a Python dictionary containing the result of
        # the above expect dict.
        # 1. Mock the urlopen context manager such that calling the read method returns
        #   a json string matching: json.dumps(expect)
        # 
        # 2. call the get_json function.
        #   - Provide the test_url and the mocked urlopen as arguments.
        # 
        # 3. Assert that the results from get_json match expect.
        # 
        # 4. Assert that the mocked urlopen was called with the test_url
        # 
        ###################################################################################

        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps(expect).encode('utf-8')

        mock_urlopen = MagicMock()
        mock_urlopen.return_value.__enter__.return_value = mock_response

        result = get_json(test_url, getter_callable=mock_urlopen)

        self.assertEqual(result, expect)

        mock_urlopen.assert_called_with(test_url)


if __name__ == '__main__':
    print(unittest.main(verbosity=1, failfast=True))
        