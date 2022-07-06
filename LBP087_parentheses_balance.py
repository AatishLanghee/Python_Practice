########################################################################################################
# Question: parentheses balance

# Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')',
# and in any positions ) so that the resulting parentheses string is valid.
# Formally, a parentheses string is valid if and only if:
# It is the empty string, or It can be written as AB (A concatenated with B), where A and B are
# valid strings, or It can be written as (A), where A is a valid string.
# Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

# input --------> a string from the user
# con ----------> no
# output -------> number of parentheses to be added

# () -------> 0
# ()( ------> 1
# ()()() ---> 0
# (((( -----> 4

# Logic:
# ~~~~~~
# 1. read a string s from the user.
# 2. if char is ( then  increment left_par counter
# 3. if char is ) then increment right_par counter.
# 4. print the value of absolute difference between left_par and right_par.
########################################################################################################
def first_approach(string: str) -> int:
    left_par: int = 0
    right_par: int = 0
    for char in string:
        if char == "(":
            left_par += 1
        else:
            right_par += 1

    return abs(left_par - right_par)


if __name__ == "__main__":
    original_string: str = input("Enter the string :")
    print(first_approach(original_string, ))
