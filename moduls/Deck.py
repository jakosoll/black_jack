import random
from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])


class Deck:
    """
    This class makes deck of 52 cards and random deal for players
    by one
    """
    RANKS = [str(i) for i in range(2, 11)] + list('JQKA')
    SUITS = 'spades diamonds clubs hearst'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.RANKS
                       for suit in self.SUITS]

    def deal_card(self):
        card = self._cards.pop(random.randrange(0, len(self._cards)))
        return f"{card.rank} of {card.suit.title()}"

    def __repr__(self):
        return '\n'.join(str(item) for item in self._cards)

    def __len__(self):
        return len(self._cards)
