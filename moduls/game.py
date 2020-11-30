from moduls.chips import Chips
from moduls.deck import Deck
from moduls.hand import PlayerHand, DealerHand
import time
from colorama import Fore


class WinChecker:
    """Проверяет оба объекта, выиграл ли кто-то из них"""
    def __init__(self, players):
        self._players = players

    def check_winner(self):
        pass


class Round:
    def __init__(self):
        time.sleep(1)
        print("Dealer takes new deck and shuffle it")
        self._deck = Deck()
        self._player_hand = PlayerHand(cards=self._deck.deal(2))
        time.sleep(1)
        print(self._player_hand)
        self._dealer_hand = DealerHand(cards=[self._deck.deal()])
        time.sleep(1)
        print(self._dealer_hand)

    def black_jack(self):
        player_score = self._player_hand.calculate_value()
        if player_score == 21 and not self._dealer_hand.has_ace_or_ten():
            return True

    def player_deals(self):
        while self._player_hand.is_need_card():
            self._player_hand.add_card(self._deck.deal())
            if self._player_hand.calculate_value() >= 21:
                break

    def dealer_deals(self):
        while self._dealer_hand.is_need_card():
            self._dealer_hand.add_card(self._deck.deal())

    def is_player_lose(self):
        return self._player_hand.check_excess()

    def is_dealer_lose(self):
        return self._dealer_hand.calculate_value() > 21

    def player_score(self):
        return self._player_hand.calculate_value()

    def dealer_score(self):
        return self._dealer_hand.calculate_value()


class Game:
    def __init__(self):
        print("Greeting!")
        time.sleep(1)
        print("It's simple Black Jack")
        self._chips = Chips()

    def start(self):
        """
        Main method where called other methods
        """
        self._chips.take_bet()

        """
        Создаем раунд, при создании печатаются руки игроков
        """
        game_round = Round()
        if game_round.black_jack():
            self._chips.win_bet()
            print('Player win!')
            return
        game_round.player_deals()
        if game_round.is_player_lose():
            self._player_lose()
            return
        game_round.dealer_deals()
        if game_round.is_dealer_lose():
            self._player_win()
            return

        if game_round.player_score() > game_round.dealer_score():
            self._player_win()
            return
        elif game_round.player_score() < game_round.dealer_score():
            self._player_lose()
            return
        else:
            time.sleep(1)
            print(Fore.WHITE + "--> Draw! <--" + Fore.RESET)
            time.sleep(2)

    def _player_win(self):
        self._chips.win_bet()
        print(Fore.GREEN + 'Player win!' + Fore.RESET)

    def _player_lose(self):
        self._chips.lose_bet()
        print(Fore.RED + 'Player lose!' + Fore.RESET)
