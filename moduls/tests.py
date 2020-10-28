from collections import namedtuple
from Hand import PlayerHand
from Deck import Deck
import unittest
from unittest.mock import patch



class PlayerHandTest(unittest.TestCase):
    def setUp(self):
        Card = namedtuple('Card', ['rank', 'suit'])
        self.cards = [
            Card('2', 'spades'),
            Card('J', 'diamonds'),
            Card('8', 'clubs')
        ]
        self.deck = Deck()
        
        self.player = PlayerHand([self.cards[0], self.cards[1]])

    def test_player_cards_count(self):
        self.assertEqual(len(self.player), 2)

    @patch("builtins.input", return_value='Y')
    def test_player_take_extra_cards(self, mock_input):
        self.player.add_card(self.cards[2])
        self.assertEqual(self.player._is_player_pass(), False)

    @patch("builtins.input", return_value="N")
    def test_player_pass(self, mock_input):
        self.player.add_card(self.cards[2])
        self.assertEqual(self.player._is_player_pass(), True)


if __name__ == "__main__":
    unittest.main()

# assert len(player) == 2, (f'{len(player)} not equal 2')
# player.add_card(deck.deal())
# assert len(player) == 3, (f'{len(player)} not equal 3')