"""Cards is a module which represents a US-standard deck of cards.

It contains class def for a Card and a Deck consisting of all 52 cards.

>>> deck = Deck()
>>> card = deck.deal()
>>> card
K♠
"""

import random

class Card:
    ''' An individual card with a suit and rank. defaults to faceup. '''
    # contructor function requires the suit and rank.
    # faceup is an optional keyword parameter defaulting to: True.
    def __init__(self, suit, rank, faceup=True):
        self.suit = suit
        self.rank = rank
        self.faceup = faceup

    def __str__(self) -> str:
        ''' The magic method __str__ determines how this object is represented when converted to a str object.

            The str representation for this object is going to be different if the card is faceup or facedown.
            Question marks are used if the card is face down.
            Example:
            >>> assert str(Card('♠', '2', faceup=False)) == '??'
            >>> assert str(Card('♠', '2', faceup=True)) == '♠2'
        '''
        rank = self.rank if self.faceup else '?'
        suit = self.suit if self.faceup else '?'
        return f'{rank}{suit}'

    def __repr__(self) -> str:
        ''' The magic method __repr__ determines how this object is represented when printed.

            str(self) calls the above __str__ method and returns the response.
            The __str__ magic method could also be called directly:
            self.__str__() == str(self)
        '''
        return str(self)

class Deck:
    ''' A deck based on a standard US card deck.
    
        Consist of 13 possible card ranks from Ace to King.
        Consist of 4 possible card suits: spades, diamond, heart, club. 
    '''
    '''
        Create class attributes containing suit and rank.
        Calling split will break these into a list.
        The split function can be used to produce simple list without the added visual clutter of the list syntax.
        Example:
        >>> assert ['♥', '♠', '♦', '♣'] == '♥ ♠ ♦ ♣'.split()
        Either is fine. However, split can make some code easier to read.
    '''
    suits = '♥ ♠ ♦ ♣'.split()
    ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self) -> None:
        ''' Create a new deck consisting of one rank for each suit.
            Produces a new list using list comprehension to loop over all of the ranks for each suit.

            Nested list comprehensions can be difficult to read.
            With for loops:
            >>> suits = '♥ ♠ ♦ ♣'.split()
            >>> ranks = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
            >>> cards = []
            >>> for suit in suits:
            ...     for rank in ranks:
            ...         cards.append(Card(suit, rank))
            >>> cards
            [A♥, 2♥, 3♥, 4♥, 5♥, 6♥, 7♥, 8♥, 9♥, 10♥, J♥, Q♥, K♥, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♦, 2♦, 3♦, 4♦, 5♦, 6♦, 7♦, 8♦, 9♦, 10♦, J♦, Q♦, K♦, A♣, 2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣]
        '''
        self.cards = [Card(s,r) for s in self.suits for r in self.ranks]

    def shufle(self) -> None:
        ''' Models the ability to shuffle a deck of cards.
            Uses the shuffle function from the random module.
        '''
        random.shuffle(self.cards)

    def deal(self, faceup=True) -> Card:
        ''' Models the ability to deal a card. '''
        card = self.cards.pop()
        card.faceup = faceup
        return card

    def __str__(self) -> str:
        ''' The majic method __str__ determines how this object is represented when converted to a str object. '''
        return ' '.join([f'{c.rank}{c.suit},' for c in self.cards])

    def __repr__(self) -> str:
        ''' The magic method __repr__ determines how this object is represented when printed. '''
        return str(self)

    def __len__(self) -> int:
        ''' The magic method __len__ determines how this opbject responds to the built-in len function.
            >>> assert len(Deck()) == 52
        '''
        return len(self.cards)


if __name__ == '__main__':
    import doctest
    print(doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL))
