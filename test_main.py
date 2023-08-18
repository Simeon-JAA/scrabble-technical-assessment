"""Testing file for main"""

from main import score_for_word, assign_player_letters
from main import find_possible_word, find_highest_score, find_highest_score_with_possible_triple
from main import highest_score_for_word_with_triplet


def test_score_for_word_base_case_1():
   """Tests base case for score_for_word (1st test case)"""

   result = score_for_word("Guardian")

   assert result == 10


def test_assign_player_letters_base_case_2():
   """Tests base case for other function (1st test case)"""

   result = assign_player_letters({"A": 6, "B": 1})

   assert len(result) == 7


def test_assign_player_letters_base_case_1():
   """Tests base case for other function (1st test case)"""

   result = assign_player_letters({"A": 6, "B": 1})

   result.sort()

   assert result == ["A","A","A","A","A","A","B"]


def test_assign_player_letters_base_case_2rhjifowa():
   """Tests base case for other function (fjweoi test case)"""

   result = assign_player_letters({"A": 5, "C": 6})

   assert "A" in result and "C" in result


def test_assign_player_letters_base_case_2rhjifawefaweowa():
   """Tests base case for other function (fjweoi test case)"""

   result = assign_player_letters({"A": 5, "C": 7})

   assert "Z" not in result


def test_find_availible_words():
   """Test for find_possible_words"""
   
   result = find_possible_word(["S","I",'M','E','O','N'], ["SIMEON"])

   assert result == "SIMEON"


def test_find_availible_words_1():
   """Test for find_possible_words"""
   
   result = find_possible_word(["S","I",'M','E','O','N'], ["SIM", "SIMEON"])

   assert result == "SIMEON"


def test_find_availible_words_3():
   """Test for find_possible_words"""
   
   result = find_possible_word(["S","I",'M','E','O','N'], ["ANGELA", "SIMEON"])

   assert result == "SIMEON"


def test_find_availible_words_4():
   """Test for find_possible_words"""
   
   result = find_possible_word(["S","I",'M','E','O','N'], ["FATSO", "ALGEBRA"])

   assert result == None


def test_find_availible_words_5():
   """Test for find_possible_words"""
   
   result = find_possible_word(["S","I",'M','E','O','N'], ["SIMEONS"])

   assert result == None


def test_find_availible_words_6():
   """Test for find_possible_words"""
   
   result = find_possible_word(["S","I",'M','E','O','N'], ["SI", "SIM", "SIMEON"])

   assert result == "SIMEON"


def test_find_highest_score_1():
   """Test for find highest score"""
   
   result = find_highest_score(["Q","U",'E','A','T','S'], ["QUE", "EATS", "ATE"])

   assert result == "QUE"


def test_find_highest_score_with_possible_triple():
   """Test for find highest score with possible triple"""
   
   result = find_highest_score_with_possible_triple(["N","A",'T','I','O','N','C','A','T'], ["QUE", "NATION", "CAT"])

   assert result == "CAT"

def test_find_highest_score_for_word_with_triple():
   """Test for find highest score with possible triple"""
   
   result = highest_score_for_word_with_triplet("CAT")

   assert result == 11


def test_find_highest_score_for_word_with_triple_1():
   """Test for find highest score with possible triple"""
   
   result = highest_score_for_word_with_triplet("DOG")

   assert result == 9


def test_find_highest_score_for_word_with_triple_1039():
   """Test for find highest score with possible triple"""
   
   result = highest_score_for_word_with_triplet("NATION")

   assert result == 8
