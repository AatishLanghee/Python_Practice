########################################################################################################
# Question: Check if String ending matches second String

# Create a function/method that takes two Strings and returns true if the first string ends with second string,
# otherwise return false.

# Input:  two strings
# Constraints: No
# Output: true or false

# abc, bc -----> true
# kalyan, an --> true
# kalyan, a ---> false

# Logic:
# ~~~~~~
# 1. read s1
# 2. read s2
# 3. from reverse compare all the characters,
# 4. len of s2 and counter
########################################################################################################
def first_approach(string_1: str, string_2: str) -> bool:
    return string_1.endswith(string_2)


def second_approach(string_1: str, string_2: str) -> bool:
    i: int = len(string_1) - 1
    count: int = 0
    for char in string_2[::-1]:
        if char == string_1[i]:
            i = i - 1
            count = count + 1

    if count == len(string_2):
        return True
    else:
        return False


if __name__ == "__main__":
    str1: str = input("Enter the first string :")
    str2: str = input("Enter the second string :")
    print(first_approach(str1, str2))
    print(second_approach(str1, str2))
