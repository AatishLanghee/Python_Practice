########################################################################################################
# Question: Swap corner words and reverse middle characters

# Write a program to take an input string and exchange the first and last word and reverse the middle word.

# input -------> a string
# con ---------> no
# output ------> a string

# example:
# Hello welcome to Java ------> Java ot emoclew Hello

# Logic:
# ~~~~~~
# 1. read a string s from the user.
# 2. until getting space character store the result in a fs.
# 3. starting fetch characters from last char to until space character store it in ls.
# 4. from end to starting point reverse each character and print.
########################################################################################################
def reverse_string(s: str) -> str:
    op_s: str = ""
    for i in range(len(s) - 1, -1, -1):
        op_s = op_s + s[i]

    return op_s


def first_approach(str_: str) -> str:
    str_list: list = str_.split(" ")
    middle_str: str = " "

    for i in range(len(str_list)-2, 0, -1):
        middle_str = middle_str + reverse_string(str_list[i]) + " "

    return str_list[-1] + middle_str + str_list[0]


def second_approach(str_: str) -> str:
    start: int = 0
    end: int = 0
    first_word: str = ""
    last_word: str = ""
    middle_string: str = ""
    for i in range(len(str_)):
        if str_[i] == " ":
            start = i
            break
        else:
            first_word = first_word + str_[i]

    for i in range(len(str_) - 1, -1, -1):
        if str_[i] == " ":
            end = i
            break
        else:
            last_word = last_word + str_[i]

    for i in range(end, start - 1, -1):
        middle_string = middle_string + str_[i]

    return reverse_string(last_word) + middle_string + first_word


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string))
    print(second_approach(string))
