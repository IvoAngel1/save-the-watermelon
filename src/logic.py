"""
logic.py
rules, display, input, score and game loop
fruit list = words.py
"""

import random
import string
import sys

import words

# a-z only
VALID_LETTERS = string.ascii_lowercase

# reasons a guess gets rejected
# used to pick what the host says
REASON_EMPTY = "empty"
REASON_TOO_LONG = "too_long"
REASON_NOT_A_LETTER = "not_a_letter"
REASON_REPEAT = "repeat"


def get_slice_count(secret_word):
    """how many slices you get. under 5 = 4, 5-8 = 6, 9+ = 7"""
    length = len(secret_word)
    if length < 5:
        return 4
    elif length < 9:
        return 6
    else:
        return 7


def get_difficulty_name(secret_word):
    """difficulty name, goes off word length too"""
    length = len(secret_word)
    if length < 5:
        return "Merienda Mode"
    elif length < 9:
        return "Fruit Stand Hustle"
    else:
        return "Abuela-Level"


def normalize_guess(raw_guess):
    """cuts the spaces and lowercases it so A and a are the same"""
    return raw_guess.strip().lower()


def validate_guess(guess, guessed_letters):
    """checks the guess. good = (True, None), bad = (False, reason)"""
    # typed nothing
    if len(guess) == 0:
        return False, REASON_EMPTY
    # more than 1 char
    if len(guess) > 1:
        return False, REASON_TOO_LONG
    # numbers, symbols, accent letters
    if guess not in VALID_LETTERS:
        return False, REASON_NOT_A_LETTER
    # already used it
    if guess in guessed_letters:
        return False, REASON_REPEAT
    return True, None


def is_correct_guess(guess, secret_word):
    """True if the letter is in the word"""
    return guess in secret_word


def count_letter(guess, secret_word):
    """how many times the letter is in the word"""
    return secret_word.count(guess)


def build_display_word(secret_word, guessed_letters):
    """makes the word the player sees, like _ a _ a _ a"""
    shown = []
    # goes thru every spot so all copies of a letter show up
    for letter in secret_word:
        if letter in guessed_letters:
            shown.append(letter)
        else:
            shown.append("_")
    return " ".join(shown)


def is_word_revealed(secret_word, guessed_letters):
    """win check. True once every letter got guessed"""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def is_out_of_slices(slices_left):
    """loss check. True when slices hit 0"""
    return slices_left <= 0


def build_watermelon_art(slices_left, total_slices):
    """the slice bar. | = still have it, x = lost it. like (||||xx)"""
    lost = total_slices - slices_left
    return "(" + "|" * slices_left + "x" * lost + ")"


# ---- host lines ----
# random.choice so he doesnt say the same thing every time

CORRECT_LINES = [
    "DING DING DING! The crowd goes BANANAS!",
    "YES! Somebody get this contestant a smoothie!",
    "Ohhh, look at you! The judges are weeping tropical tears!",
]

WRONG_LINES = [
    "BZZZT! Ooh, that one hurt. The watermelon felt that.",
    "NOPE! The studio audience gasps in horror!",
    "Wrong! Somewhere a fruit vendor just shook his head.",
]

WIN_LINES = [
    "WINNER WINNER, FRUIT SALAD DINNER! You SAVED THE WATERMELON!",
    "UNBELIEVABLE! The watermelon lives to see another day!",
]

LOSS_LINES = [
    "Aaand that's the last slice, folks. The watermelon is... gone.",
    "OH NO! Nothing left but seeds and regret!",
]

THREE_CORRECT_LINE = ("HOLD ON, HOLD ON! Three right already?! This one actually "
                      "knows their fruits, apparently!")
THREE_WRONG_LINE = ("Uh-oh... three misses. This fruit's gonna SPOIL "
                    "unless we get a comeback, people!")
BEGINNERS_LUCK_LINE = "First guess, right on the money! Beginner's luck... or a fruit PRODIGY?!"

# reason from validate_guess -> what the host says
INVALID_MESSAGES = {
    REASON_EMPTY: "You gotta type SOMETHING, superstar! One letter, please.",
    REASON_TOO_LONG: "Whoa, easy! ONE letter at a time. That's the rule.",
    REASON_NOT_A_LETTER: "That's not a letter! Numbers and symbols don't grow on trees. Try a-z.",
    REASON_REPEAT: "You already guessed that one! No slice lost - the host is feeling generous.",
}


# ---- display stuff ----

def print_banner():
    """welcome banner, shows once at the start"""
    print("=" * 56)
    print("   SAVE THE WATERMELON  -  The Tropical Fruit Game Show")
    print("=" * 56)
    print("Guess the secret fruit one letter at a time.")
    print("Every wrong guess costs the watermelon a slice!")
    print()


def show_status(secret_word, guessed_letters, slices_left, total_slices):
    """shows the word, slice bar, and what's been guessed"""
    print()
    print("Word:     " + build_display_word(secret_word, guessed_letters))
    art = build_watermelon_art(slices_left, total_slices)
    print(f"Slices:   {art}  {slices_left} left")
    if guessed_letters:
        print("Guessed:  " + ", ".join(sorted(guessed_letters)))
    else:
        print("Guessed:  (none yet)")


def print_scoreboard(stats):
    """wins, losses, streaks for this sitting"""
    print()
    print("---------------- SCOREBOARD ----------------")
    print(f"Wins: {stats['wins']}   Losses: {stats['losses']}   "
          f"Current streak: {stats['streak']}   Best streak: {stats['best_streak']}")
    print("--------------------------------------------")


# ---- input stuff ----

def get_player_guess(guessed_letters):
    """keeps asking til it gets a good new letter, then returns it"""
    # slices dont get touched in here so bad input never costs one
    while True:
        raw_guess = input("\nGuess a letter: ")
        guess = normalize_guess(raw_guess)
        is_valid, reason = validate_guess(guess, guessed_letters)
        if is_valid:
            return guess
        print(INVALID_MESSAGES[reason])


def ask_play_again():
    """y or n to play again, keeps asking til u give one"""
    while True:
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Just 'y' or 'n', my friend!")


# ---- the game ----

def play_round(secret_word):
    """plays 1 round. True = won, False = lost"""
    total_slices = get_slice_count(secret_word)
    slices_left = total_slices
    guessed_letters = set()   # set bc no dupes + quick repeat check
    correct_count = 0
    wrong_count = 0

    print(f"\nToday's difficulty: {get_difficulty_name(secret_word)}")
    print(f"The secret fruit has {len(secret_word)} letters. "
          f"You get {total_slices} slices. Good luck!")

    # game loop, goes til win or loss
    while True:
        show_status(secret_word, guessed_letters, slices_left, total_slices)
        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)

        # got it right
        if is_correct_guess(guess, secret_word):
            correct_count += 1
            times = count_letter(guess, secret_word)
            print(random.choice(CORRECT_LINES))
            print(f"'{guess}' appears {times} time(s)! No slice lost.")
            # 1st guess right = beginners luck
            if correct_count == 1 and wrong_count == 0:
                print(BEGINNERS_LUCK_LINE)
            if correct_count == 3:
                print(THREE_CORRECT_LINE)
        # got it wrong
        else:
            wrong_count += 1
            slices_left -= 1
            print(random.choice(WRONG_LINES))
            print(f"No '{guess}' in this fruit. {slices_left} slice(s) left.")
            # no comeback line if its already over
            if wrong_count == 3 and not is_out_of_slices(slices_left):
                print(THREE_WRONG_LINE)

        # check win/loss every guess
        if is_word_revealed(secret_word, guessed_letters):
            show_status(secret_word, guessed_letters, slices_left, total_slices)
            print()
            print(random.choice(WIN_LINES))
            print(f"The fruit was: {secret_word.upper()}")
            return True
        if is_out_of_slices(slices_left):
            show_status(secret_word, guessed_letters, slices_left, total_slices)
            print()
            print(random.choice(LOSS_LINES))
            print(f"The fruit was: {secret_word.upper()}")
            return False


def update_stats(stats, won):
    """updates wins/losses/streak after a round"""
    if won:
        stats["wins"] += 1
        stats["streak"] += 1
        if stats["streak"] > stats["best_streak"]:
            stats["best_streak"] = stats["streak"]
    else:
        stats["losses"] += 1
        stats["streak"] = 0   # lose = streak resets


def get_forced_word(arguments):
    """testing only. grabs the word after --word, or None"""
    if "--word" in arguments:
        position = arguments.index("--word")
        if position + 1 < len(arguments) and arguments[position + 1].isalpha():
            return arguments[position + 1].lower()
    return None


def main():
    """starts it up. banner, then rounds til the player quits"""
    forced_word = get_forced_word(sys.argv[1:])
    stats = {"wins": 0, "losses": 0, "streak": 0, "best_streak": 0}

    print_banner()
    # replay loop
    playing = True
    while playing:
        if forced_word:
            secret_word = forced_word
        else:
            secret_word = words.get_random_word()
        won = play_round(secret_word)
        update_stats(stats, won)
        print_scoreboard(stats)
        playing = ask_play_again()

    print("\nThanks for playing Save the Watermelon! Stay fresh!")
