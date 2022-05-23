########################################################################################################
# Question: Re-form the word

# A word has been split into a left part and right part.
# Re-form the word by adding both halves together changing the first character to an uppercase letter.

# input ---------> two strings from the user
# constraint ----> no
# output --------> concatenated string with caps in first character

# prakash babu ----> Prakashbabu

# Logic:
# ~~~~~~
# 1. read s1
# 2. read s2
# 3. concatenate s1 and s2, and convert first char in s1 into uppercase
# 4. print result string
########################################################################################################
def first_approach(string_1: str, string_2: str) -> str:
    return string_1.capitalize() + string_2


def second_approach(string_1: str, string_2: str) -> str:
    return string_1[0].upper() + string_1[1:] + string_2


if __name__ == "__main__":
    str1: str = input("Enter the first string :")
    str2: str = input("Enter the second string :")
    print(first_approach(str1, str2))
    print(second_approach(str1, str2))
