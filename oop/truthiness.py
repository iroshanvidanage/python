# truthiness

class Account:
    def __init__(self, name, active=True) -> None:
        self.name = name
        self.active = active
    
    def __str__(self) -> str:
        return self.name


class Accounts:
    def __init__(self, *accounts) -> None:
        self.accs = list(accounts)

    def __len__(self) -> int:
        print('Called the __len__ method.')
        return len(self.accs)
    
    def __bool__(self) -> bool:
        print('Called the __bool__ method.')
        return any(a for a in self.accs if a.active)
    
    def __str__(self) -> str:
        return ' '.join(
            str(a) for a in self.accs
        )


def demonstrate():
    # accs:Accounts = Accounts()
    accs:Accounts = Accounts(
        Account('Primary'),
        Account('Secondary', False)
    )

    print(str(accs))

    print(f'accs is {bool(accs)}')
    print(f'accs contains {len(accs)} accounts')

    if accs:
        print(f"""at least one account is active: {
            ' '.join(str(a) for a in accs.accs if a.active)
        }""")

if __name__ == '__main__':
    demonstrate()
