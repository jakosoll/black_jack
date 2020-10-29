from moduls.Chips import Chips
from moduls.Deck import Deck
from moduls.Hand import PlayerHand, DealerHand


class WinChecker:
    """Проверяет оба объекта, выиграл ли кто-то из них"""
    def __init__(self, players):
        self._players = players

    def check_winner(self):
        pass


class Round:
    def __init__(self, deck):
        self._deck = deck
        self._player_hand = PlayerHand(cards=self._deck.deal(2))
        self._dealer_hand = DealerHand(cards=self._deck.deal(2))
        self._players = [self._player_hand, self._dealer_hand]
        self._winner: object = None
        self._loser: object = None
        self._player_loose: bool = False

    def deal(self) -> None:
        for player in self._players:
            if player.is_need_card():
                player.add_card(self._deck.deal())
            

    def is_game_going(self):
        return not self._winner or not self._loser

    def _check_player(self, player):
        score = player.calculate_value()
        if score == 21:
            self._winner = player
        elif score > 21:
            self._loser = player

    def print_winner(self):
        if self._winner is PlayerHand or self._loser is DealerHand:
            print("Player win!")
        elif self._winner is DealerHand or self._loser is PlayerHand:
            print("Dealer win, Player loose!")
            self._player_loose = True

    def is_player_lose(self):
        return self._player_loose


class Game:
    def __init__(self):
        self._deck = Deck()
        self._chips = Chips()

    def start(self):
        """
        Main method where called other methods
        """
        self._chips.take_bet()
        game_round = Round(self._deck)
        continue_round = True
        while continue_round:
            game_round.deal()
            continue_round = game_round.is_game_going()
        game_round.print_winner()
        if game_round.is_player_lose():
            self._chips.lose_bet()
        else:
            self._chips.win_bet()
