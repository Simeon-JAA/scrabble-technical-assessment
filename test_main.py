"""Testing file for main"""

from main import score_for_word, assign_player_letters, find_possible_word


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

   result = assign_player_letters({"A": 5, "C": 7})

   assert "A" in result and "C" in result


def test_assign_player_letters_base_case_2rhjifawefaweowa():
   """Tests base case for other function (fjweoi test case)"""

   result = assign_player_letters({"A": 5, "C": 7})

   assert "Z" not in result


def test_find_availible_words():
   """Nice"""
   
   result = find_possible_word(["S","I",'M','E','O','N'], "SIMEON")

   assert result == "SIMEON"
