########################################################################################################
# Question: Replace Letters With Position In Alphabet

# Create a function that takes a string and replaces each letter with its appropriate position in the alphabet.
# "a" is 1, "b" is 2, "c" is 3, etc, etc.

# Note: If any character in the string isn't a letter, ignore it.

# input -----------> a string from the user
# constraint ------> non-empty string
# output ----------> position of characters separated by space

# abc -----> 1 2 3

# Logic:
# ~~~~~~
# 1. read a string s from the user.
# 2. convert all the characters into lowercase (x+32)
# 3. fetch character--> ch from the string s
# 4. ch-96

# a=97-96=1
# b=98-96=2
# c=99-96=3
########################################################################################################
def first_approach(string: str, ) -> str:
    alpha_string: str = "abcdefghijklmnopqrstuvwxyz"
    alpha_string_list: list = list(alpha_string)
    op_str: str = ""
    for char in string:
        if char in alpha_string_list:
            index: int = alpha_string_list.index(char) + 1
            op_str += str(index) + " "

    return op_str


def second_approach(string: str, ) -> str:
    op_str = ""
    for i in range(0, len(string)):
        if 'a' <= string[i] <= 'z':
            op_str += str(ord(string[i]) - 96) + " "

    return op_str


if __name__ == "__main__":
    original_string: str = input("Enter the string :")
    print(first_approach(original_string,))
    print(second_approach(original_string,))
