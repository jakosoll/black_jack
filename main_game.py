"""
Simple Black Jack game
"""
import time

from moduls.Chips import Chips
from moduls.Game import Game


def hit(deck, hand):
    hand.add_card(deck.deal())
    return hand
    # print_hand(hand)


def print_hand(hand):
    if hand is player_hand:
        hand_name = 'Player'
    else:
        hand_name = 'Dealer'
    time.sleep(1)
    print(f'{hand_name}`s cards:\n{hand}\n{hand_name}`s Hand: {hand.calculate_value()}')


def stop_game(hand):
    """Returns boolean that Hand bigger than 21 or not"""
    return not hand.calculate_value() < 21


def hit_game(hand):
    """
    This func plays game
    """
    if hand is player_hand:
        while not stop_game(hand) and ask('Hit or Stand?'):  # ask player "hit" or "stand"?
            print('Player got a card...')
            time.sleep(1)
            print_hand(hit(main_deck, hand))
    else:
        while dealer_hand.calculate_value() < 17:
            print('Dealer got a card...')
            time.sleep(1)
            if stop_game(hand):
                break
            print_hand(hit(main_deck, hand))


def ask_continue_game() -> bool:
    while True:
        time.sleep(1)
        answer = input(f'Do you want to play again? (Y/N): ').lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print('Error! Enter "Y" or "N"')


def ask(string):
    """Func takes string question
    and return True if 'Y' and False if 'N'
    """
    while True:
        time.sleep(1)
        answer = input(f'{string} (Y/N): ').lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print('Error! Enter "Y" or "N"')


if __name__ == '__main__':
    game = Game()
    continue_game: bool = True
    while continue_game:
        """Цикл основной игры"""
        game.start()
        continue_game = ask_continue_game()
    print('Bay-bay')


