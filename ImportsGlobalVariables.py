"""
Blackjack Game

This module defines the core constants used by the Blackjack game,
including card suits, ranks, point values, and the initial game state.

The card values follow standard Blackjack rules:
- Number cards are worth their face value.
- Jack, Queen, and King are worth 10 points.
- Ace initially has a value of 11 and can be adjusted to 1 when needed.
"""

import random


# All possible suits in a standard 52-card deck.
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# All possible card ranks, ordered from Two through Ace.
ranks = (
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
    'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'
)

# Maps each card rank to its corresponding Blackjack point value.
# Aces begin with a value of 11 and may later be adjusted to 1
# depending on the total value of the player's hand.
values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
}

# Controls whether the main Blackjack game loop should continue running.
playing = True