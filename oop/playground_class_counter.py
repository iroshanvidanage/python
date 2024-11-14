class Counter:
    def __init__(self):
        self.number = 0
    
    def counter(self, plus: int = 1):
        self.number += plus
    
    def __str__(self) -> str:
        return str(self.number)

if __name__ == '__main__':

    counter: Counter = Counter()
    counter.counter()
    print(counter)
    counter.counter()
    counter.counter()
    counter.counter()
    print(counter)