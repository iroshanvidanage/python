# Python Unittest - Patching

import getpass, unittest, bcrypt
from unittest.mock import patch

class UnknownUser(Exception): ...

class UserManagement:

    def __init__(self):
        self.creds = {}

    def upsert_user(self, username, password):
        self.creds[username] = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    def creds_for(self, username):
        try:
            return self.creds[username]
        except KeyError:
            raise UnknownUser(f'Authentication for {username} failed.')
        
    def authenticate(self):
        username = input('username: ')
        password = getpass.getpass('password: ').encode()
        passhash = self.creds_for(username)
        return bcrypt.checkpw(password, passhash)
    

class TestChallenge3(unittest.TestCase):

    def test_valid_users(self):
        accounts = [
            ('admin', 'secure!'),
            ('usera', 'secret!'),
            ('userb', 'stealth'),
            ('userc', 'hidden!')
        ]
        user_management = UserManagement()
        ###################################################################################
        #
        # Assignments: 
        # 
        # Test UserManagement.authenticate method by patching the input and getpass callables.
        #
        #
        # 1). For each username and password in accounts;
        #       a. Call user_management.upsert_user
        #       b. Patch the built-in input and getpass.getpass callables to return the 
        #           username and password respectively
        #       c. Assert that calling user_management.authenticate returns True
        #
        ###################################################################################
        for username, password in accounts:
            user_management.upsert_user(username=username, password=password)

            with patch('builtins.input', return_value=username), patch('getpass.getpass', return_value=password):
                self.assertTrue(user_management.authenticate())
        

    def test_invalid_users(self):
        accounts = [
            ('a', 'a'),
            ('b', 'b')
        ]
        user_management = UserManagement()
        ###################################################################################
        #
        # Assignments: 
        # 
        # Test UserManagement.authenticate method raises an UnknownUser exception
        #
        # 1). For each username and password in accounts;
        #       
        #       a. Patch the built-in input and getpass.getpass callables to return the 
        #           username and password respectively
        #
        #       b. Assert that calling user_management.authenticate raises UnknownUser exception
        #
        ###################################################################################
        for username, password in accounts:

            with patch('builtins.input', return_value=username), patch('getpass.getpass', return_value=password):
                with self.assertRaises(UnknownUser):
                    user_management.authenticate()


if __name__ == '__main__':
    print(unittest.main(verbosity=1, failfast=True))