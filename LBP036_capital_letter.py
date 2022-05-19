########################################################################################################
# Question: First capital letter

# Implement a program to return First capital letter in a String

# input -------> A string from the user
# constraint --> non-empty string
# output ------> First Capital letter

# Logic:
# ~~~~~~
# 1-----> read a string value from the user
# 2 ----> we need to check for first Capital letter,
# 3 ----> return capital letter, terminate program.

# Hello ----> H
# hEllo ----> E
# heLlo ----> L
# HellO ----> H
########################################################################################################
def capital(str_: str) -> str:
    char: str
    for char in str_:
        if char.isupper():
            return char


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(capital(string))
