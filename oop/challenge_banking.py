class Customer:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return f'Customer(name={self.name}, email={self.email})'

class Account:
    def __init__(self, customer: Customer, account_number: str) -> None:
        self.customer = customer
        self.account_number = account_number
        self.balance = 0.0
    
    def is_balance_insufficient(self, amount: float) -> bool:
        return (self.balance - amount) < 0

    def deposit(self, amount: float) -> None:
        # Implement the logic to deposit funds
        if amount <= 0:
            print('Deposit amount should be greater than Zero')
            return
        self.balance += amount
        print(f'Successfully deposited an amount of {amount}, available balance is {self.balance}.')

    def withdraw(self, amount: float) -> None:
        # Implement the logic to withdraw funds
        if amount <= 0:
            print('Withdrawal amount should be greater than Zero')
            return
        if self.is_balance_insufficient(amount):
            print('Remaining balance is not sufficient to withdraw.')
            return
        self.balance -= amount
        print(f'Successfully withdrawed an amount of {amount}, available balance is {self.balance}.')
        return

    def transfer(self, amount: float, target_account: 'Account') -> None:
        # Implement the logic to transfer funds to another account
        if amount <= 0:
            print('The amount should be greater than Zero')
            return
        if self.is_balance_insufficient(amount):
            print('Remaining balance is not sufficient to transfer.')
            return
        if self == target_account:
            print('Cannot transfer to the same account.')
        self.balance -= amount
        target_account.balance += amount
        print(f'Successfully transferred an amount of {amount}, available balance is {self.balance}.')


    def __str__(self) -> str:
        return f'Account(account_number={self.account_number}, balance={self.balance})'

# Example Usage
def test_example() -> None:
    customer1 = Customer("Alice", "alice@example.com")
    customer2 = Customer("Bob", "bob@example.com")

    account1 = Account(customer1, "12345")
    account2 = Account(customer2, "67890")

    account1.deposit(1000)
    account1.transfer(200, account2)
    account1.withdraw(100)

    print(account1)
    print(account2)

if __name__ == '__main__':
    test_example()
