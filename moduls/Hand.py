import time
from Deck import Card


class Hand:
    """
    This class create player's hand with cards
    """
    VALUES = {**{str(a): a for a in range(2, 10)}, **{'J': 10, 'Q': 10, 'K': 10, 'A': 11}}

    def __init__(self, cards: list):
        self.cards: list = cards  # empty list for cards
        self._pass: bool = False
        self.value = 0  # value of cards
        self.aces = 0  # add attribute for aces

    def add_card(self, card):
        
        if not self._pass:
            self.cards.append(card)

    def _is_player_pass(self):
        pass

    def calculate_value(self):
        self.value = 0
        self.aces = 0
        for card in self.cards:
            self.value += self.VALUES[card.rank]
            if card.rank == 'A':
                self.aces += 1
        if self.value > 21:
            self.value -= self.aces * 10
        return self.value

    def adjust_for_aces(self):
        """
        """
        pass

    def __repr__(self):
        pass

    def hit(self):
        pass

    def __len__(self):
        return len(self.cards)


class PlayerHand(Hand):

    def add_card(self, card: Card):
        self._pass = self._is_player_pass()
        super().add_card(card)
        # print(card)
        print(f'Player got {card.rank} of {card.suit.title()}')

    def _is_player_pass(self):
        while True:
            time.sleep(1)
            answer = input(f'Do you want to take another card? (Y/N): ').lower()
            if answer == 'y':
                return False
            elif answer == 'n':
                return True
            else:
                print('Error! Enter "Y" or "N"')


class DealerHand(Hand):

    def add_card(self, card):
        self._pass = self._is_player_pass()
        super().add_card(card)
        
        print(f'Dealer got {card.rank} of {card.suit.title()}')

    def _is_player_pass(self):
        return self.calculate_value() < 17
