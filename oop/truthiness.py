# truthiness

class Account:
    def __init__(self, name, active=True) -> None:
        self.name = name
        self.active = active


class Accounts:
    def __init__(self, *accounts) -> None:
        self.accs = list(accounts)

    def __len__(self):
        print('Called the __len__ method.')
        return len(self.accs)


def demonstrate():
    accs:Accounts = Accounts()

    print(f'accs is {bool(accs)}')


if __name__ == '__main__':
    demonstrate()