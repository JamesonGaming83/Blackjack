# Blackjack

A console-based Blackjack game built in Python using object-oriented programming. The game simulates a traditional game of Blackjack between the player and a computer-controlled dealer, including card dealing, betting, Ace handling, and hit-or-stand gameplay.

## Features

- Standard 52-card deck
- Randomized card shuffling
- Player and dealer hands
- Hit and stand gameplay
- Chip-based betting system
- Automatic dealer behavior
- Dynamic Ace values of 1 or 11
- Bust, win, loss, and push detection
- Input validation for player bets
- Option to play additional hands
- Object-oriented design with separate classes and modules

## How to Play

The goal of Blackjack is to get the value of your hand as close to **21** as possible without going over.

Number cards are worth their face value, while Jacks, Queens, and Kings are worth 10. Aces can be worth either 1 or 11 depending on the current value of the hand.

At the beginning of a hand:

1. A new deck is created and shuffled.
2. The player and dealer are each dealt two cards.
3. One of the dealer's cards remains hidden.
4. The player places a bet.
5. The player chooses to **Hit** or **Stand**.
6. After the player stands, the dealer draws cards until reaching at least 17.
7. The hands are compared to determine the winner.

Going over 21 results in a bust.

## Project Structure

```text
Blackjack/
├── Blackjack.py
├── CardClass.py
├── DeckClass.py
├── HandClass.py
├── ChipsClass.py
└── ImportsGlobalVariables.py
```

### `Blackjack.py`

Contains the main game loop and functions responsible for gameplay, including:

- Taking bets
- Handling hits and stands
- Displaying cards
- Determining wins and losses
- Managing additional rounds

### `CardClass.py`

Defines the `Card` class. Each card stores its:

- Suit
- Rank
- Blackjack value

### `DeckClass.py`

Defines the `Deck` class and handles:

- Creating the 52-card deck
- Shuffling cards
- Dealing cards

### `HandClass.py`

Defines the `Hand` class and handles:

- Cards currently held
- Total hand value
- Ace tracking
- Adjusting Aces from 11 to 1 when necessary

### `ChipsClass.py`

Defines the `Chips` class used to keep track of:

- Player chip balance
- Current bet
- Winning bets
- Losing bets

### `ImportsGlobalVariables.py`

Contains shared game data such as:

- Card suits
- Card ranks
- Blackjack card values
- Global game state

## Running the Game

### Requirements

- Python 3

No additional third-party Python packages are required.

### Run From Python

Clone or download the repository and navigate to the project directory.

Run the main Python file:

```bash
python Blackjack.py
```

Depending on your Python installation, you may need to use:

```bash
py Blackjack.py
```

## Example Gameplay

```text
Welcome to BlackJack! Get as close to 21 as you can without going over!
Dealer hits until she reaches 17. Aces count as 1 or 11.

How many chips would you like to bet? 20

Dealer's Hand:
 <card hidden>
 King of Hearts

Player's Hand:
 Ace of Spades
 Eight of Clubs

Would you like to Hit or Stand? Enter 'h' or 's'
```

## Concepts Demonstrated

This project demonstrates several fundamental Python programming concepts, including:

- Object-oriented programming
- Classes and objects
- Constructors
- Special methods such as `__str__`
- Functions
- Loops and conditional statements
- Lists, tuples, and dictionaries
- Exception handling
- User input validation
- Randomization
- Imports and multi-file Python projects

## Future Improvements

Possible improvements to the project include:

- Persistent chip balances between rounds
- Blackjack payout rules
- Natural Blackjack detection
- Splitting pairs
- Doubling down
- Insurance
- Improved input validation
- Graphical user interface
- Additional game settings

## License

This project is available for educational and personal use.
