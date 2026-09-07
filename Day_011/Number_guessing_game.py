from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The actual answer was {actual_answer}")


def set_difficulty():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard' ").lower()
        if level == "easy":
            return EASY_LEVEL_TURNS
        elif level == "hard":
            return HARD_LEVEL_TURNS
        else:
            print("Type a valid input")


def game():
    print(logo)
    print("welcome to the guessing game")
    print("i'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)



    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number")
        guess = int(input("make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("you've run out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again")

game()