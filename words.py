"""
words.py
the fruit list + picks one at random
miami fruit stand stuff
"""

import random

# tuple bc it never changes
# lowercase, letters only, no spaces
FRUIT_WORDS = (
    # short, under 5 = 4 slices
    "lime",
    "kiwi",
    "fig",
    "date",
    "pear",
    # medium, 5-8 = 6 slices
    "guava",
    "papaya",
    "mamey",
    "coconut",
    "mango",
    "banana",
    "plantain",
    "soursop",
    "tamarind",
    "lychee",
    "avocado",
    # long, 9+ = 7 slices
    "watermelon",
    "pineapple",
    "starfruit",
    "passionfruit",
    "dragonfruit",
    "sugarcane",
)


def get_random_word(word_list=FRUIT_WORDS):
    """picks a random fruit, gives it back lowercase"""
    return random.choice(word_list).lower()
