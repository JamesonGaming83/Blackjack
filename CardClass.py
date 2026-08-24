from ImportsGlobalVariables import *


class Card:
    """
    Represents a single playing card in a standard deck.

    Each card has a suit, rank, and Blackjack point value. The card's
    value is determined using the global 'values' dictionary based on
    the provided rank.

    Attributes:
        suit (str): The suit of the card, such as Hearts or Spades.
        rank (str): The rank of the card, such as Two, King, or Ace.
        value (int): The Blackjack point value associated with the rank.
    """

    def __init__(self, suit, rank):
        """
        Initializes a new Card object.

        Args:
            suit (str): The suit of the card.
            rank (str): The rank of the card.
        """
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        """
        Returns a readable string representation of the card.

        Returns:
            str: The card's rank and suit in the format
                 "Rank of Suit".
        """
        return self.rank + " of " + self.suit