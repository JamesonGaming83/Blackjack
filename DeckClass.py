from CardClass import *


class Deck:
    """
    Represents a standard 52-card deck used in Blackjack.

    When a Deck object is created, it automatically generates every
    combination of the available suits and ranks as Card objects.
    The deck can then be shuffled and cards can be dealt from it.

    Attributes:
        deck (list): A list containing all Card objects currently
                     remaining in the deck.
    """

    def __init__(self):
        """
        Initializes a new standard 52-card deck.

        Creates one Card object for every combination of suit and rank
        and stores each card in the deck list.
        """
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        """
        Returns a readable string representation of the entire deck.

        Each remaining card in the deck is displayed on a separate line.

        Returns:
            str: A formatted string containing all cards currently
                 remaining in the deck.
        """
        deck_comp = ' '

        for card in self.deck:
            deck_comp += '\n ' + card.__str__()

        return "The deck has: " + deck_comp

    def shuffle(self):
        """
        Randomizes the order of the cards currently in the deck.
        """
        random.shuffle(self.deck)

    def deal(self):
        """
        Removes and returns one card from the deck.

        The card is removed from the end of the deck list, reducing
        the number of cards remaining in the deck by one.

        Returns:
            Card: The Card object dealt from the deck.
        """
        single_card = self.deck.pop()
        return single_card