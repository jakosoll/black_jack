from collections import namedtuple
from moduls.hand import PlayerHand, DealerHand
from moduls.deck import Deck
from moduls.game import Round
import unittest
from unittest.mock import patch


class PlayerHandTest(unittest.TestCase):
    def setUp(self):
        Card = namedtuple('Card', ['rank', 'suit'])
        self.cards = [
            Card('2', 'spades'),
            Card('J', 'diamonds'),
            Card('8', 'clubs'),
            Card('K', 'clubs'),
            Card('10', 'spades')
        ]
        self.deck = Deck()
        
        self.player = PlayerHand([self.cards[0], self.cards[1]])
        self.dealer = DealerHand([self.cards[0], self.cards[1]])

    def test_player_cards_count(self):
        self.assertEqual(len(self.player), 2)
    
    def test_player_str(self):
        self.assertIn("Player's hand: 2 of Spades, J of Diamonds (12)", str(self.player))

    @patch("builtins.input", return_value='Y')
    def test_player_takes_extra_cards(self, mock_input):
        self.assertTrue(self.player.is_need_card())

    @patch("builtins.input", return_value="N")
    def test_player_pass(self, mock_input):
        self.assertFalse(self.player.is_need_card())

    def test_player_excess(self):
        """
        Тест перебора карт
        """
        self.player.add_card(self.cards[3])
        self.assertTrue(self.player.check_excess())

    def test_player_calculate_value(self):
        self.player.add_card(self.cards[4])
        self.assertEqual(self.player.calculate_value(), 22)


class DealerHandTest(unittest.TestCase):
    """
    Тестируем диллера
    """
    def setUp(self) -> None:
        Card = namedtuple('Card', ['rank', 'suit'])
        self.cards = [
            Card('2', 'spades'),
            Card('J', 'diamonds'),
            Card('8', 'clubs'),
            Card('K', 'clubs')
        ]
        self.deck = Deck()
        self.dealer = DealerHand([self.cards[1]])

    def test_dealer_has_ace_or_ten(self):
        """Тест что у диллера есть туз или картинка"""
        self.assertTrue(self.dealer.has_ace_or_ten())

    def test_dealer_str(self):
        self.assertIn("Dealer's hand: J of Diamonds", str(self.dealer))

    def test_dealer_takes_extra_cards(self):
        self.dealer.add_card(self.cards[2])
        self.assertFalse(self.dealer.is_need_card())


class RoundTest(unittest.TestCase):
    def setUp(self) -> None:
        self.game_round = Round()

    def test_cards_amount(self):
        self.assertEqual(len(self.game_round._dealer_hand), 1)
        self.assertEqual(len(self.game_round._player_hand), 2)


class DeckTest(unittest.TestCase):
    def setUp(self) -> None:
        self.deck = Deck()

    def test_deck_give_two_cards(self):
        cards = self.deck.deal(amount=2)
        self.assertEqual(len(cards), 2)


if __name__ == "__main__":
    unittest.main()
