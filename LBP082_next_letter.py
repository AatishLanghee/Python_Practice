########################################################################################################
# Question: Change Every Letter to the Next Letter

# Write a function that changes every letter to the next letter:

# "a" becomes "b"
# "b" becomes "c"
# "d" becomes "e"
# and so on ...
# 'x' becomes 'y'
# 'y' becomes 'z'
# 'z' becomes ''

# note: there is no z's in test cases, be happy.

# input ------> a string from the user
# cons -------> no
# output -----> modified string

# Logic:
# ~~~~~~
# 1. read a string s from the user.
# 2. fetch char by char from s and print s+1 until if s is not equal to 'z'

# abc ----> bcd

# a=97+1=98->b
# b=98+1=99->c
# c=99+1=100->d
########################################################################################################
def first_approach(str_: str) -> str:
    op_string: str = ""
    for char in str_:
        if char == " ":
            op_string += char
        else:
            if char == 'z':
                op_string += ""
            else:
                op_string += chr(ord(char) + 1)
    return op_string


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string))
