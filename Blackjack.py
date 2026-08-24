"""
Blackjack Game

This module contains the main game logic for a command-line Blackjack game.

The program manages player input, betting, card dealing, hit/stand decisions,
win and loss conditions, and the main game loop. Supporting classes such as
Deck, Hand, and Chips are imported from their respective modules.

The goal is to get as close to 21 as possible without going over. The dealer
continues drawing cards until reaching a hand value of at least 17.
"""

from ImportsGlobalVariables import *
from DeckClass import *
from HandClass import *
from ChipsClass import *

def take_bet(chips):
    """
    Prompts the player to enter a valid chip bet.

    The function continues requesting input until the player enters an
    integer that does not exceed their available chip total.

    Args:
        chips (Chips): The player's Chips object containing their
                       current balance and bet.
    """
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break


def hit(deck, hand):
    """
    Deals one card to a hand and adjusts the value for any Aces.

    Args:
        deck (Deck): The deck from which the card is dealt.
        hand (Hand): The hand receiving the card.
    """
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    """
    Prompts the player to choose whether to hit or stand.

    Choosing hit deals another card to the player's hand. Choosing stand
    ends the player's turn and allows the dealer to begin playing.

    Args:
        deck (Deck): The active deck of cards.
        hand (Hand): The player's current hand.
    """
    global playing

    while True:
        x = input("\nWould you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue

        break


def show_some(player, dealer):
    """
    Displays the player's cards while hiding one of the dealer's cards.

    This function is used during the player's turn so that the dealer's
    complete hand remains unknown.

    Args:
        player (Hand): The player's hand.
        dealer (Hand): The dealer's hand.
    """
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    """
    Displays all cards and hand values for both the player and dealer.

    Args:
        player (Hand): The player's hand.
        dealer (Hand): The dealer's hand.
    """
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)

    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    """
    Handles the result when the player's hand exceeds 21.

    The player's current bet is deducted from their chip total.

    Args:
        player (Hand): The player's hand.
        dealer (Hand): The dealer's hand.
        chips (Chips): The player's chip balance.
    """
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    """
    Handles the result when the player wins the hand.

    The player's current bet is added to their chip total.

    Args:
        player (Hand): The player's hand.
        dealer (Hand): The dealer's hand.
        chips (Chips): The player's chip balance.
    """
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    """
    Handles the result when the dealer's hand exceeds 21.

    The player's current bet is added to their chip total.

    Args:
        player (Hand): The player's hand.
        dealer (Hand): The dealer's hand.
        chips (Chips): The player's chip balance.
    """
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    """
    Handles the result when the dealer wins the hand.

    The player's current bet is deducted from their chip total.

    Args:
        player (Hand): The player's hand.
        dealer (Hand): The dealer's hand.
        chips (Chips): The player's chip balance.
    """
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    """
    Handles a tied hand between the player and dealer.

    No chips are won or lost during a push.

    Args:
        player (Hand): The player's hand.
        dealer (Hand): The dealer's hand.
    """
    print("Dealer and Player tie! It's a push.")


# Main game loop.
while True:

    # Display the game introduction and basic Blackjack rules.
    print(
        'Welcome to BlackJack! Get as close to 21 as you can without going over!\n'
        'Dealer hits until she reaches 17. Aces count as 1 or 11.'
    )

    # Create and shuffle a new deck.
    deck = Deck()
    deck.shuffle()

    # Create the player's hand and deal two starting cards.
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    # Create the dealer's hand and deal two starting cards.
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Create the player's chip balance.
    player_chips = Chips()

    # Ask the player how many chips they want to bet.
    take_bet(player_chips)

    # Display the hands while keeping one dealer card hidden.
    show_some(player_hand, dealer_hand)

    # Continue the player's turn until they stand or bust.
    while playing:

        # Ask the player whether they want to hit or stand.
        hit_or_stand(deck, player_hand)

        # Display the updated hands.
        show_some(player_hand, dealer_hand)

        # End the player's turn if their hand exceeds 21.
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If the player has not busted, begin the dealer's turn.
    if player_hand.value <= 21:

        # Dealer must continue hitting until reaching at least 17.
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

            # Display all cards once the dealer begins playing.
            show_all(player_hand, dealer_hand)

            # Determine the result of the hand.
            if dealer_hand.value > 21:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand, dealer_hand)

    # Display the player's remaining chip balance.
    print("\nPlayer's winnings stand at", player_chips.total)

    # Ask whether the player wants to start another hand.
    new_game = input(
        "Would you like to play another hand? Enter 'y' or 'n' "
    )

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        break