########################################################################################################
# Question: Stuttering Function

# write a function that shutters a word as if someone is struggling to read it.
# The first two letters are repeated twice with an ellipsis ... , and then the word is pronounced with a question mark?

# input ------------> a string
# constraint --------> no
# output -----------> xx... xx... ~~~~~~~?

# abc =====> ab...ab...abc?

# Logic:
# ~~~~~~
# 1. read a string from the user
# 2. create an empty string
# 3. copy first two characters and ...
# 4. copy first two characters and ...
# 5. copy the content of s to new string
# 6. append ? mark at the end.
# 7. print new string
########################################################################################################
def first_approach(str_: str) -> str:
    return str_[:2] + "..." + str_[:2] + "..." + str_ + "?"


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string))
    