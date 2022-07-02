########################################################################################################
# Question: Returns the middle character of a string

# create a function that takes a string and returns, the middle character(s).
# if the word's length is odd return the middle character.
# if the word's length is even, return the middle two characters.

# input -----> a string from the user
# constraint-> no
# output ----> middle character(s)

# abc -----> 3 -> Odd ====> b
# xyz -----> 3 -> Odd ====> y
# abcde ---> 5 -> Odd ====> c
# abcd ----> 4 -> Even ===> bc
# middle --> 6 -> Even ===> dd

# Logic:
# ~~~~~~
# 1. read a string from the user.
# 2. store length of the string in n.
# 3. if n is even ====> s[n/2-1],s[n/2]
# 4. if n is odd =====> s[n/2]
########################################################################################################
def first_approach(str_: str) -> str:
    if len(str_) % 2 == 1:
        return str_[len(str_) // 2]
    return str_[(len(str_) // 2) - 1: (len(str_) // 2) + 1]


if __name__ == "__main__":
    string: str = input("Enter the ZIP code :")
    print(first_approach(string))
