# Use a while loop to let the user guess again
# Change the for loop so that you keep the previous correct answers
import random
import hangman_art
from hangman_words import word_list


lives = 6
placeholder = ""
correct_letters = []

chosen_word = random.choice(word_list)

print(chosen_word)
word_length = len(chosen_word)

print(hangman_art.logo)
print(hangman_art.HANGMANPICS[6])

for word in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False

while not game_over:
    print(f"**********{lives}/6 Lives LEFT**********")
    guess = input("Guess a letter in the chosen word.").lower()

    if guess in correct_letters:
        print (f"You already guessed that letter: {guess}")

    display = ""



    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"


    if "_" not in display:
        game_over = True
        print("********** YOU WON **********")
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the chosen word.")
        if lives == 0:
            game_over = True
            print(f"********** YOU LOSE :( The correct word was: {chosen_word}**********")

    print(hangman_art.HANGMANPICS[lives])
    print(display)






