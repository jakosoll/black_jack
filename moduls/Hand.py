import time


class Hand:
    """
    This class create player's hand with cards
    """
    VALUES = {**{str(a): a for a in range(2, 10)}, **{'J': 10, 'Q': 10, 'K': 10, 'A': 11}}

    def __init__(self, cards: list):
        self.cards = cards  # empty list for cards
        self.value = 0  # value of cards
        self.aces = 0  # add attribute for aces

    def add_card(self, card):
        self.cards.append(card)

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
        return ', '.join(str(item) for item in self.cards)

    def hit(self):
        pass


class PlayerHand(Hand):
    def __init__(self, cards: list):
        super().__init__(cards)
        self._pass: bool = False

    def add_card(self, card):
        self._pass = self._is_player_pass()
        if not self._pass:
            self.cards.append(card)
            print(f'Player got {card.rank} of {card.suit}')

    @staticmethod
    def _is_player_pass():
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
        self.cards.append(card)
        print(f'Dealer got {card}')
