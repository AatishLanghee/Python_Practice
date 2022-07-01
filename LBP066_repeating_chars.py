########################################################################################################
# Question: Repeating characters

# Create a method that takes a string and returns a string in which each character is repeated once.

# input ---------------> String from the user
# constraint ----------> No
# output --------------> String

# String ------> SSttrriinngg

# Logic:
# ~~~~~~
# 1. read a string from the user as s
# 2. create a new string ns
# 3. copy each character twice to the ns
# 4. print ns
########################################################################################################
def first_approach(str_: str) -> str:
    op_: str = ""
    char: str
    for char in str_:
        op_ = op_ + 2 * char
    return op_


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string))
