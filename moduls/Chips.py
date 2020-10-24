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
                print(f'Your have {self.total}$')
                self.bet = int(input('Enter your bet: '))
            except ValueError:
                print('Please, enter your bet by numbers')

            else:
                if self.bet > self.total:
                    print('Your bet bigger than you have')
                else:
                    break
        print(f'Your bet is {self.bet}')

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
