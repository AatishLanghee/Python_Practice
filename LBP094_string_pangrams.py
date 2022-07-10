########################################################################################################
# Question: Pangrams

# Implement a program to check whether the given string pangram or not.
# A pangram is a string that contains all the letters of the English alphabet.
# An example of a pangram is "The quick brown fox jumps over the lazy dog"

# input ----> a string from the user
# con ------> non-empty string
# output ---> Yes or No

# Logic:
# ~~~~~~
# 1. read a string from the user.
# 2. create an array with 26 elements and initialize them to 0.
# 3. fetch char one by one from the string.
# 4. initialize array index of char to 1
# 5. check if 0 present in array, if 0 present, return "Pangrams", else "Not Pangrams"
########################################################################################################
def first_approach(str_: str) -> str:
    alpha_list: list = list("abcdefghijklmnopqrstuvwxyz")
    pangrams_list: list = alpha_list.copy()
    received_char_list: list = []
    char: str
    for char in str_.lower():
        if char in alpha_list:
            alpha_list.remove(char)
            received_char_list.append(char)
        else:
            if char in received_char_list:
                continue

    if len(received_char_list) == len(pangrams_list):
        return "Pangrams"
    return "Not Pangrams"


def second_approach(str_: str) -> str:
    alpha_list: list = [0] * 26
    char: str
    for char in str_.lower():
        if char.isalpha():
            alpha_list[ord(char) - 97] = 1

    if 0 in alpha_list:
        return "Not Pangrams"

    return "Pangrams"


def third_approaches(str_: str) -> str:
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in str_.lower():
            return "Not Pangrams"

    return "Pangrams"


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string,))
    print(second_approach(string,))
    print(third_approaches(string,))
