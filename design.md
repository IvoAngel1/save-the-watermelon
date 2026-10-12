# Design

## idea

make a simple fruit guessing game in python. kind of like hangman, but with watermelon slices.

the goal is to guess the fruit before losing all the slices.

## rules

- pick a random fruit
- show blanks for the letters
- one letter per guess
- make guesses lowercase so `A` and `a` are the same
- don't allow numbers, symbols, repeats or more than 1 letter
- right = show the letter, keep slices
- wrong = lose 1 slice
- no slices left = lose. show the word
- all letters guessed = win
- ask to play again when the round ends

## difficulty

- 1-4 letters = 4 slices / Merienda Mode
- 5-8 letters = 6 slices / Fruit Stand Hustle
- 9+ letters = 7 slices / Abuela-Level

## main files

- `words.py` - the fruit list and random fruit
- `logic.py` - checks the guesses, letters and slices
- `game.py` - prints the game, gets input, score and replay

i split it into 3 files so it isn't all in one place.

## main variables

- `secret_word` - fruit to guess
- `guessed_letters` - letters already used
- `total_slices` - starting slices
- `slices_left` - slices still there
- `correct_count` - right guesses
- `wrong_count` - wrong guesses
- `stats` - wins, losses and streaks

## other things

- `guessed_letters` is a set so it doesn't store repeats
- `build_display_word()` shows `_` until a letter gets guessed
- `validate_guess()` checks if the input is okay
- `is_word_revealed()` checks for a win
- `is_out_of_slices()` checks for a loss
- `--word guava` lets me choose the word for testing
- the host has different messages, plus the 3 right / 3 wrong messages

## game order

start -> pick fruit -> show blanks -> ask for a letter -> check guess -> win or lose -> show score -> play again or quit
