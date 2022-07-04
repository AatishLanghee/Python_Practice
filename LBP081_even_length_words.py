########################################################################################################
# Question: Even Length Words

# Write a program to print even length words in a string?

# input -----> a string from the user
# con -------> no
# output ----> list of strings with even length

# hello welcome to java ----> to java
# a ab abc abcd abcde abcdef --> ab abcd abcdef

# Logic:
# ------
# 1. read a sentence from the user as s.
# 2. fetch one by one token from string s.
# 3. check the length of the token is even or not
# 4. if even print that token
# 5. else continue
########################################################################################################
def first_approach(str_: str) -> str:
    op_str: list = []
    for word in str_.split(" "):
        if len(word) % 2 == 0:
            op_str.append(word)

    return " ".join(op_str)


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string))
