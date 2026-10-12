# Number Guessing Game

A simple Python project built to practice **Python fundamentals** and understand how **binary search** works.

## About

This project is a number-guessing game where either the player or the computer tries to guess a number between **1 and 100**.

There are two game modes:

* **Player guesses:** The computer generates a random number, and the player tries to guess it.
* **Computer guesses:** The player thinks of a number, and the computer uses a binary-search approach to find it.

The project also records game results in a `game_stats.json` file.

## Features

* Random number generation
* Interactive command-line gameplay
* Input validation
* Two different guessing modes
* Binary search implementation
* Game statistics stored in JSON
* Handles invalid or missing JSON data

## How It Works

### 1. Player Guesses

In this mode, the computer randomly selects a number between 1 and 100.

The player repeatedly enters a guess:

* If the guess is too low, the program says **"Too low!"**
* If the guess is too high, the program says **"Too high!"**
* If the guess is correct, the game displays the number of guesses taken.

The program also prevents guesses outside the range of 1–100 and handles non-numeric input.

### 2. Computer Guesses Using Binary Search

In this mode, the player thinks of a number between 1 and 100.

The computer starts with:

```text
low = 1
high = 100
```

It then guesses the middle of the current range:

```python
guess = (low + high) // 2
```

The player responds with:

* `h` — the secret number is **higher**
* `l` — the secret number is **lower**
* `c` — the computer guessed correctly

Based on the response, the computer eliminates half of the remaining possibilities and continues searching.

For example:

```text
Possible numbers: 1–100
Computer guesses: 50

If higher:
Possible numbers: 51–100
Computer guesses: 75

If lower:
Possible numbers: 51–74
Computer guesses: 62
```

This is the basic idea behind **binary search**: repeatedly divide the search space in half.

## Binary Search Concept

If there are `n` possible numbers, binary search requires approximately:

```text
O(log₂ n)
```

guesses in the worst case.

For numbers from 1 to 100, the computer needs at most about **7 guesses** when the responses are consistent.

This makes binary search much more efficient than checking every number one by one.

## Saving Game Statistics

After a game ends, the program saves information to:

```text
game_stats.json
```

Each game stores:

* Game ID
* Game type
* Number of guesses/steps
* Secret number

For example:

```json
{
    "data": [
        {
            "id": 1,
            "Game type": "Computer guesses",
            "Guesses": 6,
            "Secret number": 73
        }
    ]
}
```

The program creates an empty data structure if the JSON file does not exist or cannot be decoded.

## Requirements

* Python 3.x

The project only uses Python's standard library:

```python
import random
import json
```

No external packages are required.

## How to Run

Clone or download the project, then run:

```bash
python main.py
```

The program will ask:

```text
Would you like to guess the number
(enter 'p') or have the computer guess your number
(enter 'c')?
```

Enter:

```text
p
```

to play the normal guessing game, or:

```text
c
```

to let the computer guess your number.

## Project Structure

```text
.
├── main.py
├── game_stats.json    # Created automatically after playing
└── README.md
```

## What I Learned

This project was created as a learning exercise to practice:

* Python functions
* `while` loops
* `if/elif/else` statements
* User input
* Exception handling with `try/except`
* Random number generation
* Reading and writing JSON files
* Basic file handling
* Lists and dictionaries
* The **binary search algorithm**
* Algorithmic efficiency and `O(log n)` complexity

## Future Improvements

Possible improvements include:

* Add a difficulty system with different number ranges
* Add a maximum number of guesses
* Add a score system
* Display previous game statistics
* Improve input validation in computer-guess mode
* Add a replay option without restarting the program
* Add tests for the binary search logic
