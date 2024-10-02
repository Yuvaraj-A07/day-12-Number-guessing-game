#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo)
computer = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100")
level = input("choose the difficulty : type 'easy' or hard :").lower()
is_game_over = True
while (is_game_over):
    if (level == 'easy'):
        attempts = 10
        while attempts != 0:
            print(
                f"You have {attempts} attempts remaining to guess the number")
            guess = int(input("Make a guess : "))
            if (guess == computer):
                print(f"You guessed correctly, The number is {guess}.")
                attempts = 0
            elif (guess > computer):
                print("Too high")
                print("Guess again")
                attempts -= 1
            else:
                print("Too low")
                print("Guess again")
                attempts -= 1
            if (attempts == 0 and not (guess == computer)):
                print("Sorry you have no more attempts, you lose the game")
                is_game_over = False
            if (attempts == 0):
                is_game_over = False

    else:
        attempts = 5
        while attempts != 0:
            print(
                f"You have {attempts} attempts remaining to guess the number")
            guess = int(input("Make a guess : "))
            if (guess == computer):
                print(f"You guessed correctly, The number is {guess}.")
                attempts = 0
            elif (guess > computer):
                print("Too high")
                print("Guess again")
                attempts -= 1
            else:
                print("Too low")
                print("Guess again")
                attempts -= 1
            if (attempts == 0 and not (guess == computer)):
                print("Sorry you have no more attempts, you lose the game")
                is_game_over = False
            if (attempts == 0):
                is_game_over = False
