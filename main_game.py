"""
Simple Black Jack game
"""
import time


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


if __name__ == '__main__':
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
