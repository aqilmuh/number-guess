import random
import json
from json import JSONDecodeError

filename = "game_stats.json"
try:
    with open(filename, "r") as f:
        data = json.load(f)
except (FileNotFoundError, JSONDecodeError):
    data = {"data": []}

def save_stats(game_type, guesses, secret_number):
    game_data = {
        "id": len(data["data"]) + 1,
        "Game type": game_type,
        "Guesses": guesses,
        "Secret number": secret_number
    }
    data["data"].append(game_data)
    with open("game_stats.json", "w") as f:
        json.dump(data, f, indent=4)
        print("Exiting the app. Goodbye!")

def player_guess():
    print("Guess a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    guesses = 0
    # print(secret_number)  # For testing purposes, you can remove this line in production
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            guesses += 1
            if 1 <= guess <= 100:
                if guess < secret_number:
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You've guessed the number {secret_number} correctly!")
                    print(f"It took you {guesses} guesses.")
                    break
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    save_stats("Player guesses", guesses, secret_number)

def computer_guess():
    print("""
How to play:
Think of a number between 1 and 100, and I will try to guess it.
Respond with 'h' if it's higher, 'l' if lower, or 'c' if correct.
""")
    low = 1
    high = 100
    steps = 0
    while True:
        guess = (low + high) // 2
        steps += 1

        response = input(f"Is your number {guess}? (h/l/c): ").lower()
        if response == 'h':
            low = guess + 1
        elif response == 'l':
            high = guess - 1
        elif response == 'c':
            print(f"Yay! I guessed your number {guess} correctly!")
            print(f"It took me only {steps} step to guess the number." if steps == 1 else f"It took me {steps} steps to guess the number.")
            break
        else:
            print("Invalid input. Please respond with 'h' for higher, 'l' for lower, or 'c' for correct.")
        if low > high:
            print("Hmm, it seems there's a contradiction in your responses. Let's start over.")
            break

    save_stats("Computer guesses", steps, guess)

def main():
    print("Welcome to the Number Guessing Game!")
    mode = input("Would you like to guess the number (enter 'p') or have the computer guess your number (enter 'c')? ").lower()
    if mode == 'p':
        player_guess()
    elif mode == 'c':
        computer_guess()
    else:
        print("Invalid input. Please enter 'p' or 'c'.")
    

if __name__ == "__main__":
    main()
#     print("Welcome to the Number Guessing Game!")
#     mode = input("Would you like to guess the number (enter 'p') or have the computer guess your number (enter 'c')? ").lower()
#     if mode == 'p':
#         player_guess()
#     elif mode == 'c':
#         computer_guess()
#     else:
#         print("Invalid input. Please enter 'p' or 'c'.")