########################################################################################################
# Question: C*ns*r*d Str*ngs

# Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s.
# Luckily, I've been able to find the vowels that were removed.

# Given a censored string and a string of the censored vowels, return the original uncensored string.

# input --------> original & replacement strings
# con ----------> no
# output -------> updated string after replacement

# w*lc*m*,eoe ====> welcome

# Logic:
# ~~~~~~
# 1. read a string s1 from the user
# 2. read replacement string s2 from the user
# 3. fetch char by char from s1 and if * found replace that char with char in s2.
########################################################################################################
def first_approach(string: str, vow_string: str) -> str:
    count: int = 0
    op_string: str = ""
    for char in string:
        if char == "*":
            op_string += vow_string[count]
            count += 1
        else:
            op_string += char
    return op_string


if __name__ == "__main__":
    original_string: str = input("Enter the string :")
    vowels_string: str = input("Enter the vowels string :")
    print(first_approach(original_string, vowels_string))
