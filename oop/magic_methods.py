from . import display # imports from __init__.py

class Account:
    def __init__(self):
        print('New account initialized.')
    
    def __init__(self, name: str, balance: float =0) -> None:
        self.name = name
        self.balance = balance



def demonstrate():
    # account_1: Account = Account()
    account_a: Account = Account('savings', 200.42)
    account_b: Account = Account('checking', 400.42)

    display('str(account_a)', str(account_a))
    display('str(account_b)', str(account_b))


if __name__ == '__main__':
    demonstrate()