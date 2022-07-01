########################################################################################################
# Question:
# Andy, Ben and Charlotte are playing a board game.
# The three of them decided to come up with a new scoring system.
# A player's first initial ("A","B" & "C") denotes that players scoring a single point.
# Given a string of capital letters. returns an array of the player's scores.

# input --------------> A String
# constraint ---------> No
# output -------------> score

# A ---------------> 1 0 0
# AB --------------> 1 1 0
# ABC -------------> 1 1 1
# AABBC -----------> 2 2 1

# Logic:
# ~~~~~~
# 1. read a string from the user as s   //ABC
# 2. fetch every character from s as ch //A,B,C
# 3. if ch is equal to A then a++
# 4. if ch is equal to B then b++
# 5. if ch is equal to C then c++
# 6. print a b c
########################################################################################################
from typing import Tuple, Any


def first_approach(str_: str) -> Tuple[Any, Any, Any]:
    score_count: dict = {"A": 0, "B": 0, "C": 0}
    char: str
    for char in str_:
        score_count[char] = score_count[char] + 1

    return score_count["A"], score_count["B"], score_count["C"]


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string))
