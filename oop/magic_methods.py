from . import display # imports from __init__.py

class Account:
    def __init__(self) -> None:
        print('New account initialized.')
    
    def __init__(self, name: str, balance: float =0) -> None:
        self.name = name
        self.balance = balance

    def __str__(self) -> str:
        return f'account: {self.name} balance: {self.balance}'

    def __float__(self) -> float:
        return self.balance

    def __int__(self) -> int:
        return int(self.balance)
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__} ({self.balance})'
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    def __lt__(self, other):
        return self.balance < other.balance
    
    def __le__(self, other):
        return self.balance <= other.balance
    
    def __gt__(self, other):
        return self.balance > other.balance
    
    def __ge__(self, other):
        return self.balance >= other.balance


class Person:
    def __init__(self, name: str, surname: str = None) -> None:
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f'{self.name} {self.surname or ""}'


class Player:
    def __init__(self, handle):
        self.handle = handle

    def __eq__(self, other):
        return self.handle == other.handle


def demonstrate():
    # account_1: Account = Account()
    account_a: Account = Account('savings', 200.42)
    account_b: Account = Account('checking', 400.42)

    display('str(account_a)', str(account_a))
    display('str(account_b)', str(account_b))
    display('int(account_b)', int(account_b))
    display('float(account_b)', float(account_b), indent=1)
    display('repr(account_a)', repr(account_a))

    display('account_a > account_b', account_a > account_b, indent=1)
    display('account_a < account_b', account_a < account_b, indent=1)
    display('account_a >= account_b', account_a >= account_b, indent=1)
    display('account_a <= account_b', account_a <= account_b, indent=1)
    display('account_a == account_b', account_a == account_b, indent=1)
    display('account_a != account_b', account_a != account_b, indent=1)


if __name__ == '__main__':
    demonstrate()
    p = Person('Ada', 'Lovelace')
    print(p)

    p_a: Player = Player('smasher')
    p_b: Player = Player('crasher')
    p_c: Player = Player('smasher')

    assert p_a == p_c
    assert p_a != p_b
