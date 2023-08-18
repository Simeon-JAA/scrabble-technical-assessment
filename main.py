"""Technical assessment file"""

import random

AVAILIBLE_LETTERS = {"A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3,
      "H": 2, "I": 9, "J": 1, "K": 1, "L": 4, "M": 2, "N": 6,
        "O": 8, "P": 2, "Q": 1, "R": 6, "S": 4, "T": 6, "U": 4,
          "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1}

with open('dictionary.txt', "r") as f:
    POSSIBLE_WORDS = f.read().split('\n')

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


def highest_score_for_word_with_triplet(word: str) -> int:
    """Return the score of the word"""

    word = list(word.upper())

    letter_group_allocation = {"EAIONRTLSU" : 1,
                        "DG": 2,
                        "BCMP": 3,
                        "FHVWY": 4,
                        "K": 5,
                        "JX": 8,
                        "QZ": 10
                        }

    list_of_possible_points = []

    for index, _ in enumerate(word):
        total_points = 0 
        word_copy = word.copy()
        word_copy[index] = word_copy[index].lower()
        for l in word_copy:
            if l.islower():
                l = l.upper()
                for letter_group in letter_group_allocation.keys():
                    if l in letter_group:
                        total_points += 3 * letter_group_allocation[letter_group]
            else:
                for letter_group in letter_group_allocation.keys():
                    if l in letter_group:
                        total_points += letter_group_allocation[letter_group]
        list_of_possible_points.append(total_points)
         
    return max(list_of_possible_points)      


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


def find_possible_word(player_letters: list[str], availible_words: list[str]) -> str:
    """Find a possible word"""
   
    word_to_make = ""

    list_of_possible_words = []
    
    for word in availible_words:
        player_letters_copy = player_letters.copy()
        word_to_make_copy = word_to_make

        for letter in word:
            print(word_to_make)

            if letter not in player_letters_copy:
                break

            if letter in player_letters_copy and letter != word[-1]:
                player_letters_copy.remove(letter)
                word_to_make_copy += letter

            if letter in player_letters_copy and letter == word[-1]: 
                player_letters_copy.remove(letter)
                word_to_make_copy += letter
                if word_to_make_copy in availible_words:
                    list_of_possible_words.append(word_to_make_copy)
                    

    if len(list_of_possible_words) !=  0:
        list_of_possible_words.sort(key=len, reverse=True)
        print(list_of_possible_words)
        return list_of_possible_words[0]
    else:
        return None
        
    
    return None


def find_highest_score(player_letters: list[str], availible_words: list[str]) -> str:
    """Find a highest scoring word"""
   
    word_to_make = ""

    list_of_possible_words = []
    
    for word in availible_words:
        player_letters_copy = player_letters.copy()
        word_to_make_copy = word_to_make

        for letter in word:
            print(word_to_make)

            if letter not in player_letters_copy:
                break

            if letter in player_letters_copy and letter != word[-1]:
                player_letters_copy.remove(letter)
                word_to_make_copy += letter

            if letter in player_letters_copy and letter == word[-1]: 
                player_letters_copy.remove(letter)
                word_to_make_copy += letter
                if word_to_make_copy in availible_words:
                    list_of_possible_words.append(word_to_make_copy)
                    

    if len(list_of_possible_words) !=  0:

        possible_words_as_scores = list(map(score_for_word, list_of_possible_words))
        
        index_of_highest_score = 0 

        highest_score = 0
        for index, score in enumerate(possible_words_as_scores):
            if score > highest_score:
                highest_score = score
                index_of_highest_score = index
        return list_of_possible_words[index_of_highest_score]
    
    else:
        return None
        
    
# 1. Find the highest scoring word if any one of the letters can score triple.

def find_highest_score_with_possible_triple(player_letters: list[str], availible_words: list[str]) -> str:
    """Find a highest scoring word"""
   
    word_to_make = ""

    list_of_possible_words = []
    
    for word in availible_words:
        player_letters_copy = player_letters.copy()
        word_to_make_copy = word_to_make

        for letter in word:
            print(word_to_make)

            if letter not in player_letters_copy:
                break

            if letter in player_letters_copy and letter != word[-1]:
                player_letters_copy.remove(letter)
                word_to_make_copy += letter

            if letter in player_letters_copy and letter == word[-1]: 
                player_letters_copy.remove(letter)
                word_to_make_copy += letter
                if word_to_make_copy in availible_words:
                    list_of_possible_words.append(word_to_make_copy)
                    

    if len(list_of_possible_words) !=  0:

        possible_words_as_scores = list(map(highest_score_for_word_with_triplet, list_of_possible_words))
        
        index_of_highest_score = 0 

        highest_score = 0
        for index, score in enumerate(possible_words_as_scores):
            if score > highest_score:
                highest_score = score
                index_of_highest_score = index
        return list_of_possible_words[index_of_highest_score]
    
    else:
        return None
        
    


   
if __name__ == "__main__":

    print(POSSIBLE_WORDS)
    pass