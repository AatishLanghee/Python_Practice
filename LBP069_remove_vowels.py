########################################################################################################
# Question: Remove Every vowel from a String

# Create a function that takes a string and returns a new string with all vowels removed.

# input -------------> a string
# constraints -------> No
# output ------------> a string

# welcome ------> wlcm
# prakash ------> prksh

# Logic:
# ~~~~~~
# 1. read a string from the user as s1
# 2. create an empty string as s2
# 3. copy each character from s1 to s2 if ch is not a vowel
# 4. print s2
########################################################################################################
def first_approach(str_: str) -> str:
    op_: str = ""
    for char in str_.lower():
        if char not in ("a", "e", "i", "o",  "u"):
            op_ = op_ + char

    return op_


def second_approach(str__: str) -> str:
    import re
    op__: str = re.sub("[aeiou]", "", str__)
    return op__


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string))
    print(second_approach(string))
