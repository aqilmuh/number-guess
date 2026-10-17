# Searching Algorithms in Python

A small collection of three terminal projects that explore **divide-and-conquer searching algorithms**, namely binary search and ternary-style (three-way) search, through games and puzzles.

Instead of reading about the algorithms in the abstract, you play with them: guess a number, let the computer guess yours, find a fake coin with a balance scale, or hunt down a hidden point on a grid.

---

## 📑 Table of Contents

- [Projects at a Glance](#-projects-at-a-glance)
- [1. Number Guessing Game](#1-number-guessing-game-number_guesspy)
- [2. Counterfeit Coin Finder](#2-counterfeit-coin-finder-counterfeit_coinpy)
- [3. Coordinate Guess](#3-coordinate-guess-coordinate_guesspy)
- [Installation](#-installation)
- [Future Ideas](#-future-ideas)

---

## 🗂 Projects at a Glance

| Project | File | Algorithm | Idea |
|---|---|---|---|
| Number Guessing Game | `number_guess.py` | Binary search | Guess a number from 1 to 100, or let the computer guess yours |
| Counterfeit Coin Finder | `counterfeit_coin.py` | Ternary (3-way) search | Find the one lighter coin among *n* coins using a balance scale |
| Coordinate Guess | `coordinate_guess.py` | 2D binary search | Find a hidden `(x, y)` point on a grid |

---

## 1. [Number Guessing Game](https://github.com/aqilmuh/number-guess/tree/main/number-guess) (`number_guess.py`)

A classic higher/lower game with two modes. It is the most direct demonstration of **binary search**: each guess cuts the remaining range in half.

**Current features**

- 🎮 **Player mode (`p`)**: the computer picks a secret number from 1 to 100 and you guess it, getting "too low" or "too high" hints.
- 🤖 **Computer mode (`c`)**: you think of a number and the computer finds it using binary search, guessing the midpoint each time. You answer `h` (higher), `l` (lower), or `c` (correct).
- ✅ Input validation for non-numbers, out-of-range guesses, and invalid responses.
- 🕵️ Detects contradictory answers in computer mode (when the search range becomes empty) and stops the game.
- 💾 Saves every finished game to `game_stats.json` (game type, number of guesses, secret number).

**Example: computer guesses your number (you're thinking of 37)**

```text
Welcome to the Number Guessing Game!
Would you like to guess the number (enter 'p') or have the computer guess your number (enter 'c')? c

How to play:
Think of a number between 1 and 100, and I will try to guess it.
Respond with 'h' if it's higher, 'l' if lower, or 'c' if correct.

Is your number 50? (h/l/c): l
Is your number 25? (h/l/c): h
Is your number 37? (h/l/c): c
Yay! I guessed your number 37 correctly!
It took me 3 steps to guess the number.
Exiting the app. Goodbye!
```

**Example: you guess the computer's number**

```text
Guess a number between 1 and 100.
Enter your guess (1-100): 50
Too high! Try again.
Enter your guess (1-100): 25
Too low! Try again.
...
```

**Saved stats (`game_stats.json`)**

```json
{
    "data": [
        {
            "id": 1,
            "Game type": "Computer guesses",
            "Guesses": 3,
            "Secret number": 37
        }
    ]
}
```

**Run it**

```bash
python number_guess.py
```

---

## 2. [Coordinate Guess](https://github.com/aqilmuh/number-guess/tree/main/coordinate-guess) (`coordinate_guess.py`)

Extends binary search to **two dimensions**. A secret `(x, y)` coordinate is hidden on an `n × n` grid, and the program finds it by running a binary search on the x-axis and the y-axis at the same time.

**Current features**

- 🎯 Randomly generates a secret coordinate on a grid (default size `n = 100`).
- 🧭 Narrows the x range and y range independently with every guess.
- 📈 Returns both the found coordinate and the number of steps it took, which stays small even on large grids (about 7 steps for a 100 × 100 grid).
- 🧩 `grid_search(x_size, y_size, secret_x, secret_y)` is a reusable function, and the grid doesn't have to be square.

**Example output**

```text
Secret coordinate: (37, 82)
Found secret coordinate: [37, 82] with 6 steps
```

**Run it**

```bash
python coordinate_guess.py
```

---

## 3. [Counterfeit Coin Finder](https://github.com/aqilmuh/number-guess/tree/main/counterfeit-coin) (`counterfeit_coin.py`)

A classic logic puzzle: among *n* coins, exactly one counterfeit is **lighter** than the rest. Using a balance scale, find it in as few weighings as possible.

Instead of splitting in two, this program splits the remaining coins into **three groups** and weighs two of them against each other. Each weighing cuts the search space to a third, so the coin is found in about log₃(n) weighings.

**Current features**

- 🔢 Works for any number of coins you enter, not just multiples of 3 (group sizes are rounded up and the leftover group is smaller).
- ⚖️ Shows which coins to put on the left pan (Group 1) and the right pan (Group 2); the remaining coins form an implicit Group 3 that stays off the scale.
- 🔁 Narrows the range after every weighing based on your answer:
  - `l`: the **left** side is lighter, so the coin is in Group 1
  - `r`: the **right** side is lighter, so the coin is in Group 2
  - `s`: the scales are the **same**, so the coin is in Group 3 (off the scale)

**Example: 9 coins, counterfeit is coin 8**

```text
Enter the number of coins: 9
Group 1: 
1 2 3 
Group 2: 
4 5 6 
Which scale is lighter? (l or r or s): s
Group 1: 
7 
Group 2: 
8 
Which scale is lighter? (l or r or s): r
The counterfeit coin is: 8
```

**Run it**

```bash
python counterfeit_coin.py
```

---


## 🛠 Installation

All three projects use only Python's standard library (`random` and `json`), so there are **no external dependencies**.

**Requirements**

- Python 3.6 or newer (f-strings are used)
- Git (optional, for cloning)

**Steps**

1. **Clone the repository**

   ```bash
   git clone https://github.com/aqilmuh/number-guess.git
   cd number-guess
   ```

2. **Check your Python version**

   ```bash
   python --version
   ```

   On some systems you may need to use `python3` instead of `python` in all commands.

3. **Run any project**

   ```bash
   python number_guess.py
   python counterfeit_coin.py
   python coordinate_guess.py
   ```

> 💡 `number_guess.py` creates a `game_stats.json` file in the folder you run it from. If you don't want it tracked by Git, add it to your `.gitignore`.

---

## 💡 Future Ideas

**Shared improvements**

- [ ] A single main menu (`main.py`) to launch all three projects
- [ ] Move the algorithms into reusable functions or modules and add unit tests
- [ ] Add `if __name__ == "__main__":` guards so files can be imported without running (`coordinate_guess.py` and `counterfeit_coin.py` currently run on import)
- [ ] Clean up commented-out legacy code

**Number Guessing Game**

- [ ] Choose difficulty or a custom range (1–10, 1–1000, and so on)
- [ ] Limited-attempts mode and hints based on the optimal number of guesses
- [ ] A stats viewer showing win history, averages, and best scores from `game_stats.json`
- [ ] Save stats for incomplete or contradictory games too

**Coordinate Guess**

- [ ] Let the user choose the grid size and the secret coordinate
- [ ] Visualize the shrinking search area step by step (ASCII grid or `matplotlib`)
- [ ] Extend to 3D (`x, y, z`) or higher dimensions
- [ ] Compare against a linear search to show the speed-up

**Counterfeit Coin Finder**

- [ ] Auto-simulate the scale with a hidden random counterfeit, instead of asking the user to answer
- [ ] Handle the case where the counterfeit may be heavier *or* lighter
- [ ] Validate input (non-numbers, `n < 1`, invalid scale responses)
- [ ] Display the minimum possible number of weighings (⌈log₃ n⌉) for comparison

---

## 📄 License
[MIT](https://mit-license.org/)
