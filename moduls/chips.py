import time
from colorama import Fore

class Chips:
    """"""

    def __init__(self):
        self.total = 200  # кол-во фишек в начале игры
        self.bet = 0  # ставка

    def take_bet(self):
        """
        Incoming arg - from Chips class.
        Func ask player about his bet.
        Func have no return value.
        """
        while True:
            try:
                time.sleep(1)
                print(Fore.CYAN + f'Your have {self.total}$')
                time.sleep(1)
                self.bet = int(input('Enter your bet: '))
            except ValueError:
                print(Fore.RED + 'Please, enter your bet by numbers' + Fore.RESET)

            else:
                if self.bet > self.total:
                    print(Fore.RED + 'Your bet bigger than you have' + Fore.RESET)
                else:
                    break
        print(Fore.CYAN + f'Your bet is {self.bet}' + Fore.RESET)

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def __repr__(self):
        return self.total
