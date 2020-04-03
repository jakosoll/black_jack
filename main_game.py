"""
Simple Black Jack game
"""
import time
import random

SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    """
    This class makes cards for game
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    """
    This class makes deck of 52 cards, shuffle them and deal for players
    by one
    """
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)

    def __repr__(self):
        return '\n'.join(str(item) for item in self.deck)


class Hand:
    """
    This class create player's hand with cards
    """
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
            self.value += VALUES[card.rank]
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


class Chips:
    """"""

    def __init__(self):
        self.total = 200  # кол-во фишек в начале игры
        self.bet = 0  # ставка

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    """
    Incoming arg - from Chips class.
    Func ask player about his bet.
    Func have no return value.
    """
    while True:
        try:
            print(f'Your have {player_chips.total}$')
            chips.bet = int(input('Enter your bet: '))
        except ValueError:
            print('Please, enter your bet by numbers')

        else:
            if chips.bet > player_chips.total:
                print('Your bet bigger than you have')
            else:
                break


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


print('[- Welcome to simple Black Jack -]')
time.sleep(2)
score: bool = True
player_chips = Chips()  # created player's chips (100)
while score:
    main_deck = Deck()
    main_deck.shuffle()
    time.sleep(1)
    take_bet(player_chips)  # take player's bet
    time.sleep(1)
    print(f'Your bet is {player_chips.bet}$')
    player_hand = Hand()  # create player's Hand
    dealer_hand = Hand()  # create dealer's Hand
    print_hand(hit(main_deck, dealer_hand))
    time.sleep(1)
    hit(main_deck, player_hand)
    print_hand(hit(main_deck, player_hand))
    time.sleep(1)
    hit_game(player_hand)  # player decide to take more cards or not
    if 21 < player_hand.calculate_value():
        print('Player lose!')
        time.sleep(1)
        player_chips.lose_bet()
        print(f'Player`s score: {player_chips.total}')
        if ask('Wanna play more?'):
            continue
        else:
            score = False
            print("Bye!")
    elif player_hand.calculate_value() == 21:
        print('Black Jack! You win!')
        time.sleep(1)
        player_chips.win_bet()
        print(f'Player`s score: {player_chips.total}')
        if ask('Wanna play more?'):
            continue
        else:
            score = False
            print("Bye!")

    hit_game(dealer_hand)  # dealer games
    if 21 > dealer_hand.calculate_value() > player_hand.calculate_value():
        print('Player lose! Dealer Win!')
        time.sleep(1)
        player_chips.lose_bet()
        print(f'Player`s score: {player_chips.total}')
        if ask('Wanna play more?'):
            continue
        else:
            score = False
            print("Bye!")
    elif dealer_hand.calculate_value() == 21:
        print('Black Jack! Dealer win!')
        time.sleep(1)
        player_chips.win_bet()
        print(f'Player`s score: {player_chips.total}')
        if ask('Wanna play more?'):
            continue
        else:
            score = False
            print("Bye!")
    else:
        print('Player win!')
        time.sleep(1)
        player_chips.win_bet()
        print(f'Player`s score: {player_chips.total}')
        if ask('Wanna play more?'):
            continue
        else:
            score = False
            print("Bye!")
