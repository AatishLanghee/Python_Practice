########################################################################################################
# Question: Index of first vowel

# create a function that returns the index of first vowel in a string

# input ------> a string
# con --------> no
# output -----> an int value

# test ------> e(1) -------------> 1
# welcome ---> e(1),o(4),e(6) ---> 1
# python ----> o(4) -------------> 4

# Logic:
# ~~~~~~
# 1. read a string from the user as s.
# 2. read character from string s one by one and store in ch.
# 3. if first occurrence of ch is in vowels, then return index.
########################################################################################################
from typing import Any


def first_approach(str_: str) -> Any:
    char: str
    for i, char in enumerate(str_.lower()):
        if char in ("a", "e", "i", "o", "u",):
            return i
    return None


if __name__ == "__main__":
    string: str = input("Enter the ZIP code :")
    print(first_approach(string))
