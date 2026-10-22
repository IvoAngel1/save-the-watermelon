"""
logic.py
just the rules. no print or input in here, thats game.py
easier to test this way
"""

import string

# a-z only
VALID_LETTERS = string.ascii_lowercase

# reasons a guess gets rejected
# game.py uses these to pick what the host says
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
