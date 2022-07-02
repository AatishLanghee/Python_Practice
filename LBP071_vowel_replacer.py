########################################################################################################
# Question: VOWEL REPLACER

# Create a function that replaces all the vowels in a string with a specified character,

# input -----------> A string from the user and a character
# cons ------------> no
# output ----------> A string

# welcome,% ----> w%lc%m%

# Logic:
# ~~~~~~
# 1. read a string from the user as s
# 2. read replacement character as ch from the user.
# 3. declare a string as rs.
# 4. read each character c from s.
# 5. if it is vowel then copy ch to rs.
# 6. if it is not vowel then copy s[i] to rs.
########################################################################################################
def first_approach(str_: str, char_: str) -> str:
    op_: str = ""
    for char in str_.lower():
        if char in ("a", "e", "i", "o", "u",):
            op_ = op_ + char_
        else:
            op_ = op_ + char
    return op_


if __name__ == "__main__":
    string: str = input("Enter the string :")
    char__: str = input("Enter the character :")
    print(first_approach(string, char__))
