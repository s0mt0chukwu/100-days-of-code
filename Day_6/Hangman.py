import random

from hangman_words import word_list
from hangman_art import stages, logo

print(logo
      )
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

Game_over = False
correct_letters = []

while not Game_over:
    print(f"***********************<???{lives} LIVES LEFT************************")
    guess = input("Guess a letter").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess},  that is not in the . Youlose a life")
        if lives == 0:
            Game_over = True

            print(f"************************IT WAS{chosen_word} YOU LOSE************************")

    print(stages[lives])

    if "_" not in display:
        Game_over = True
        print("*****************************You win*****************************")



