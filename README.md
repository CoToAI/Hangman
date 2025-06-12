# 🪓 Hangman Game (Python)

A simple command-line implementation of the classic **Hangman** game written in Python. This beginner-friendly project demonstrates control flow, loops, conditional logic, user input, and external file management in Python.

---

## 📜 Description

This Hangman game selects a random word from a list and allows the user to guess one letter at a time. The player starts with 6 lives, and each incorrect guess reduces a life. The game continues until the player correctly guesses all letters or runs out of lives.

### Key Features:
- Random word selection from an external list (`hangman_words.py`)
- ASCII art visuals from `hangman_art.py`
- Letter placeholders updated dynamically
- Input validation for repeated guesses
- Tracks and displays remaining lives

---

## 🧠 What I Learned

This project helped me learn and apply several fundamental programming concepts:

- **While Loops**: Replaced the `for` loop with a `while` loop to allow the player to keep guessing until the game ends.
- **Persistent State**: Modified the game to retain previously guessed correct letters, improving user experience.
- **Conditional Logic**: Learned how to manage game states (win/lose) using `if` statements and flags like `game_over`.
- **Lists and Strings**: Practiced manipulating strings and using lists to store guessed letters.
- **Basic Debugging**: By printing out the chosen word during development, I could test and debug game logic.

---

