########################################################################################################
# Question: VALID ZIP CODE

# zipcodes consists of 5 consecutive digits.
# Given a string, write a function to determine whether the input is a valid zip code.
# a valid zipcode is as follows

# 1. must contain only numbers.
# 2. it should not contain any spaces.
# 3. length should be only 5.

# input ------> A string
# constraint -> no
# output -----> true or false

# 11111 ----> true
# 4564 -----> false
# 123 4-----> false

# Logic:
# ~~~~~~
# 1. read a string s from the user
# 2. for each digit increment counter.
# 3. if counter is 5, then it is valid
# 4. else it is invalid.

# Regular Expression:

# [aeiou] -> Search vowels
# [^aeiou] -> Search not vowels (^ is NOT)
# [x|o] -> search x or o
# [02468] -> -> Search even digit
# [^02468] or [13579] -> Search odd digit
# [2357] -> Search prime digit
# [0-9][0-9][0-9][0-9][0-9] -> want exact 5 digit where each digit can be in 0-9
# [0-9]{5} -> want exact 5 digit where each digit can be in 0-9
# [6789][0-9]{9} -> first number must be from 6-9 and remaining number can be 0-9
########################################################################################################
def first_approach(str_: str) -> str:
    if len(str_) != 5:
        return "Invalid ZIP"
    for char in str_:
        if not char.isdigit():
            return "Invalid ZIP"
    return "Valid ZIP"


def second_approach(string_: str) -> str:
    if len(string_) != 5:
        return "Invalid ZIP"
    for char in string_:
        try:
            isinstance(int(char), int)
        except Exception as e:
            print(e)
            return "Invalid ZIP"
    return "Valid ZIP"


def third_approach(string__: str) -> str:
    import re
    op_ = re.fullmatch("[0-9]{5}", string__)
    if op_:
        return "Valid ZIP"
    return "Invalid ZIP"


if __name__ == "__main__":
    string: str = input("Enter the ZIP code :")
    print(first_approach(string))
    print(second_approach(string))
    print(third_approach(string))
