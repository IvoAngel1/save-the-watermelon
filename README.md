# Save the Watermelon

this is a fruit guessing game i made in python. it runs in the terminal.

## how it works

- the game picks a fruit
- you guess 1 letter at a time
- right guess = letter shows up
- wrong guess = lose a watermelon slice
- repeat or bad input = try again. no slice lost
- guess the word before the slices run out and you win
- you can play again. the score stays until you close the game

## slices

- under 5 letters = 4 slices (Merienda Mode)
- 5 to 8 letters = 6 slices (Fruit Stand Hustle)
- 9 or more = 7 slices (Abuela-Level)

## run it

Python 3.8 or newer. no extra installs.

open a terminal in the project folder:

```bash
python src/game.py
```

windows can also use `py src/game.py`.

if i want to test a certain fruit:

```bash
python src/game.py --word guava
```

## files

- `src/game.py` - main game, input, host messages, scoreboard
- `src/logic.py` - guesses, slices and game rules
- `src/words.py` - fruit list and random word
- `docs/design.md` - my plan
- `docs/pseudocode.md` - game steps
- `docs/test-plan.md` - tests and results

## extra stuff

- miami fruit stand theme and game show host
- 3 difficulty levels
- slice bar like `(||||xx)`
- score, wins, losses and streaks
- messages for first right guess, 3 right and 3 wrong guesses

## limits

- one letter at a time, `a-z` only
- no full word guesses
- scoreboard resets when you exit
- fruit words are inside `words.py`
