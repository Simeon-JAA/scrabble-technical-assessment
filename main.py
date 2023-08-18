"""Technical assessment file"""

import random

AVAILIBLE_LETTERS = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3,
      "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6,
        "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4,
          "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1}

with open('dictionary.txt', "r") as f:
    POSSIBLE_WORDS = f.read().replace('\n', ' ')

def score_for_word(word: str) -> int:
    """Return the score of the word"""

    word = word.upper()

    letter_group_allocation = {"EAIONRTLSU" : 1,
                        "DG": 2,
                        "BCMP": 3,
                        "FHVWY": 4,
                        "K": 5,
                        "JX": 8,
                        "QZ": 10
                        }

    total_points = 0
    
    for letter in word:
        for letter_group in letter_group_allocation.keys():
            if letter in letter_group:
                total_points += letter_group_allocation[letter_group]
            
    return total_points


def assign_player_letters(availible_letters: dict) -> list[str]:
    """Returns a players hand"""

    alphabet = list(availible_letters.keys())

    hand_to_return = []

    length_of_player_hand = 7

    while length_of_player_hand > 0:
        
        letter_to_add = alphabet[random.randrange(len(alphabet))]
        
        if availible_letters[letter_to_add] == 0:
            continue
        else:
            hand_to_return.append(letter_to_add)
            availible_letters[letter_to_add] -= 1 
            length_of_player_hand -= 1
    
    return hand_to_return

# 1. Find a valid word formed 
# from the seven tiles.

def find_possible_word(letters: list[str], availible_words: str) -> str:
    """Find a possible word"""
    #GO THROUGH EACH AVAILIBLE WORD
    #FOR EACH LETTER IN THAT WORD
    #IF THE LETTER IS IN THE PLAYER HAND
    pass


if __name__ == "__main__":

    pass