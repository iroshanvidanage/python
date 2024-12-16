# Abstract method
from abc import ABC, abstractmethod

class Renderable(ABC):
    @abstractmethod
    def render(self): ...


class Text(Renderable):
    def __init__(self, text):
        self.text = text
    
    def render(self):
        return self.text


class UppercaseText(Text):
    def render(self):
        return self.text.upper()


class Money(Renderable):
    def __init__(self, money, currency='$'):
        self.money = money
        self.currency = currency
    
    def render(self):
        return f'{self.currency} {self.money}'


if __name__ == '__main__':
    # Renderable() - Cannot be directly instantiated.
    
    renderables = [
        Text('Hello person'),
        UppercaseText('Hello person'),
        Money(3.14)
    ]

    for renderable in renderables:
        print(renderable.render())