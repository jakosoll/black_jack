"""
Simple Black Jack game
"""
import time

from moduls.chips import Chips
from moduls.game import Game


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


if __name__ == '__main__':
    game = Game()
    continue_game: bool = True
    while continue_game:
        """Цикл основной игры"""
        game.start()
        continue_game = ask_continue_game()
    print('Bay-bay')


