# userman module

class UnknownUser(Exception):
    '''Exception: Unknown username'''

class UserManagement:
    '''Fake User management system.'''

    def __init__(self) -> None:
        self.creds = {}
    
    def upsert_user(self, username: str, password: str) -> None:
        self.creds[username.lower()] = password
    
    def creds_for(self, username: str) -> None:
        try:
            return self.creds[username.lower()]
        except KeyError:
            raise UnknownUser(f'Authentication for {username} failed.')
    
    def authenticate(self, username: str, password: str) -> bool:
        try:
            creds = self.creds_for(username)
        except UnknownUser:
            return False
        except:
            raise

        return creds == password
    