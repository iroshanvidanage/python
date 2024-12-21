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

    def deposit(self, amount: float) -> None:
        # Implement the logic to deposit funds

    def withdraw(self, amount: float) -> None:
        # Implement the logic to withdraw funds

    def transfer(self, amount: float, target_account) -> None:
        # Implement the logic to transfer funds to another account

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
