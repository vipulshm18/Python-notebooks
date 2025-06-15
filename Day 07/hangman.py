#Step 1
import random
from hangman_art import logo, stages
from hangman_words import word_list

lives = 6
print(logo)

chosen_word = random.choice(word_list)
masked_word = ""

for letters in range(0, len(chosen_word)):
    masked_word += "_"
print("Word to guess: " + masked_word)

game_over = False
correct_guess = []

while not game_over:
    print(f"************************{lives}/6 LIVES LEFT************************")
    guess = input("Guess a letter: ").lower()
    if guess in correct_guess:
        print(f"You've already guessed {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guess.append(guess)
        elif letter in correct_guess:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word, you lose a life.")
        if lives == 0:
            game_over = True
            print(f'******************************IT WAS {chosen_word}, You lose!******************************')

    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[lives])
