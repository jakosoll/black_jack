from moduls.Chips import Chips
from moduls.Deck import Deck
from moduls.Hand import PlayerHand, DealerHand


class Game:
    def __init__(self):
        self._deck = Deck()
        self._chips = Chips()
        self._player_hand = PlayerHand()
        self._dealer_hand = DealerHand()

    def start(self):
        """
        Main method where called other methods
        """
        self._chips.take_bet()
        for _ in range(2):
            self._player_hand.add_card(self._deck.deal_card())
            self._dealer_hand.add_card(self._deck.deal_card())
        while True:
            pass



