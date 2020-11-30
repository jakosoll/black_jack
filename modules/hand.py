import time
from colorama import Fore
from .deck import Card
from typing import List


class Hand:
    """
    This class create player's hand with cards
    """
    VALUES = {**{str(a): a for a in range(2, 11)}, **{'J': 10, 'Q': 10, 'K': 10, 'A': 11}}
    _value: int = 0

    def __init__(self, cards: List[Card]):
        self.cards: list = cards  # empty list for cards

    def add_card(self, card: Card):
        self.cards.append(card)
        self.calculate_value()

    def is_need_card(self) -> bool:
        pass

    def calculate_value(self) -> int:
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
        return self._value

    def __str__(self):
        pass

    def __len__(self):
        return len(self.cards)


class PlayerHand(Hand):

    def add_card(self, card):
        super().add_card(card)
        # print(card)
        print(Fore.GREEN + f'Player got {card.rank} of {card.suit.title()}' + Fore.RESET)
        time.sleep(1)
        print(self)

    def is_need_card(self):
        while True:
            time.sleep(1)
            answer = input(Fore.CYAN + f'Do you want to take another card? (Y/N): ' + Fore.RESET).lower()
            if answer == 'y':
                return True
            elif answer == 'n':
                return False
            else:
                print('Error! Enter "Y" or "N"')

    def check_excess(self):
        return self.calculate_value() > 21

    def __str__(self):
        cards = [f'{card.rank} of {card.suit.title()}' for card in self.cards]
        return Fore.GREEN + "Player's hand: " + ", ".join(cards) + f" ({self.calculate_value()})" + Fore.RESET


class DealerHand(Hand):

    def add_card(self, card):
        super().add_card(card)
        print(Fore.BLUE + f'Dealer got {card.rank} of {card.suit.title()}'+ Fore.RESET)
        time.sleep(1)
        print(self)

    def is_need_card(self):
        return self.calculate_value() < 17

    def has_ace_or_ten(self):
        return self.calculate_value() >= 10

    def __str__(self):
        cards = [f'{card.rank} of {card.suit.title()}' for card in self.cards]
        return Fore.BLUE + "Dealer's hand: " + ", ".join(cards) + f" ({self.calculate_value()})" + Fore.RESET
