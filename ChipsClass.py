class Chips:
    """
    Represents a player's chip balance and current bet.

    The player begins with a default balance of 100 chips. The class
    keeps track of the player's current bet and updates their balance
    depending on whether the bet is won or lost.

    Attributes:
        total (int): The player's current number of chips.
        bet (int): The number of chips placed on the current hand.
    """

    def __init__(self):
        """
        Initializes a new Chips object.

        The player starts with 100 chips and no active bet.
        """
        self.total = 100
        self.bet = 0

    def win_bet(self):
        """
        Adds the current bet to the player's total after a win.
        """
        self.total += self.bet

    def lose_bet(self):
        """
        Subtracts the current bet from the player's total after a loss.
        """
        self.total -= self.bet