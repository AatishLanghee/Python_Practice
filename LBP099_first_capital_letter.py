########################################################################################################
# Question: Capitalize Every word first character

# Implement a program to capitalize first letter of each word in a string.

# input ----> a string from the user
# con ------> non-empty string
# output ---> a string with capitalization

# welcome to programming -----> Welcome To Programming

# Logic:
# ~~~~~~
# 1. read a string s from the user.
# 2. divide the string into tokens.
# 3. print each token in the following format.
#
# 	first character convert into Caps and remaining characters
########################################################################################################
def first_approach(str_: str) -> str:
    word_lst: list = str_.split(" ")
    op_list: list = []
    word: str
    for word in word_lst:
        op_list.append(word.capitalize())

    return " ".join(op_list)


if __name__ == "__main__":
    string: str = input("Enter a string :")
    print(first_approach(string,))
