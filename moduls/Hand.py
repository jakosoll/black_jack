class Hand:
    """
    This class create player's hand with cards
    """
    VALUES = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}

    def __init__(self):
        self.cards = []  # empty list for cards
        self.value = 0  # value of cards
        self.aces = 0  # add attribute for aces

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        self.value = 0
        self.aces = 0
        for card in self.cards:
            self.value += self.VALUES[card.rank]
            if card.rank == 'Ace':
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
    def __init__(self):
        super().__init__()

    def add_card(self, card):
        self.cards.append(card)
        print(f'Player got {card}')


class DealerHand(Hand):
    def __init__(self):
        super().__init__()

    def add_card(self, card):
        self.cards.append(card)
        print(f'Dealer got {card}')
