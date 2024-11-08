class Counter:
    
    def __init__(self):
        self.number = 0
    
    def count(self):
        self.number += 1
    
    def out(self) -> int:
        return self.number
    
    def __str__(self) -> str:
        return str(self.number)
    

c: Counter = Counter()
print(c.out())
c.count()
print(c.out())
print(c)
print(c.number)