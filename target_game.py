"""
TARGET GAME MODULE
"""
from typing import List
import string
import random
import sys

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    grid = [[],[],[]]
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i].append(random.choice(string.ascii_uppercase))
    return grid

def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    pass



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    # words = sys.stdin.readlines()
    # return words
    words = []
    for word in input().split():
        if word not in words:
            words.append(word)
    return words

print(get_user_words())

def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass
