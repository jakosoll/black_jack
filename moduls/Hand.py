import time
from Deck import Card
from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """
    interface observer declare update method for Publishers using for notice his subscribers
    """

    @abstractmethod
    def update(self, publisher):
        pass


class Publisher(ABC):
    """
    Publisher inteface declare any methods for obey subscribers
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Attach observer to publisher"""
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Detach observer to publisher"""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notice subscribers"""
        pass


class GameObserver(Observer):
    """
    Watching for status of player and dealer
    """
    looser = None
    winner = None

    def update(self, subject) -> None:
        if subject._value > 21:
            self.looser = subject
        if subject.


class Hand(Publisher):
    """
    This class create player's hand with cards
    """
    VALUES = {**{str(a): a for a in range(2, 10)}, **{'J': 10, 'Q': 10, 'K': 10, 'A': 11}}

    _observers: List[Observer] = []
    _pass: bool = False
    _value: int = 0

    def __init__(self, cards: List[Card]):
        self.cards: list = cards  # empty list for cards

    def add_card(self, card: Card):
        self.cards.append(card)
        self._calculate_value()
        self.notify()

    def is_need_card(self) -> bool:
        pass

    def _calculate_value(self) -> None:
        """Calc value of hand"""
        value = 0
        aces = 0
        for card in self.cards:
            value += self.VALUES[card.rank]
            if card.rank == 'A':
                aces += 1
        if value > 21:
            value -= aces * 10
        self._value = value

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        """Start update in observer list"""
        for observer in self._observers:
            observer.update(self)

    def __len__(self):
        return len(self.cards)


class PlayerHand(Hand):

    def add_card(self, card):
        super().add_card(card)
        # print(card)
        print(f'Player got {card.rank} of {card.suit.title()}')

    def is_need_card(self):
        while True:
            time.sleep(1)
            answer = input(f'Do you want to take another card? (Y/N): ').lower()
            if answer == 'y':
                return True
            elif answer == 'n':
                self._pass = True
                return False
            else:
                print('Error! Enter "Y" or "N"')

    def __repr__(self):
        cards = [f'{card.rank} of {card.suit.title()}' for card in self.cards]
        return ", ".join(cards)


class DealerHand(Hand):

    def add_card(self, card):
        super().add_card(card)
        print(f'Dealer got {card.rank} of {card.suit.title()}')

    def is_need_card(self):
        self._pass = self._calculate_value() < 17
        return self._pass
