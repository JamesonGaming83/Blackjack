from DeckClass import *


class Hand:
    """
    Represents a hand of cards in a Blackjack game.

    The Hand class stores the cards currently held by a player or dealer,
    calculates the total Blackjack value of those cards, and keeps track
    of Aces so their values can be adjusted when necessary.

    Attributes:
        cards (list): A list containing the Card objects in the hand.
        value (int): The current total Blackjack value of the hand.
        aces (int): The number of Aces currently counted as 11.
    """

    def __init__(self):
        """
        Initializes an empty Blackjack hand.

        A new hand begins with no cards, a total value of zero,
        and no Aces.
        """
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """
        Adds a card to the hand and updates the hand's total value.

        If the added card is an Ace, it is also added to the Ace count
        so its value can be adjusted later if the hand exceeds 21.

        Args:
            card (Card): The Card object to add to the hand.
        """
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        """
        Adjusts the value of Aces when the hand would otherwise bust.

        Each Ace initially has a value of 11. While the hand's value is
        greater than 21, an Ace can be changed from 11 to 1 by subtracting
        10 from the total value.
        """
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1