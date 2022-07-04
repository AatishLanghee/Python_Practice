########################################################################################################
# Question: Removing Duplicate Characters from a string

# Given a string S, the task is to remove all the duplicates in the given string.

# input --------> a string from the user
# con ----------> remove all duplicates
# output -------> a string without duplicates

# hello -----> helo
# program ---> progam

# Logic:
# ~~~~~~
# 1. read a string s from the user.
# 2. fetch one by one character from s.
# 3. compare the character ch with remaining all the characters.
# 4. if duplicate found, move next char to current position.
# 5. print updated string.
########################################################################################################
def first_approach(str_: str) -> str:
    op_list: list = []
    char: str
    for char in str_:
        if char not in op_list:
            op_list.append(char)

    return "".join(op_list)


def second_approach(str_: str) -> str:
    op_str = ""
    for char in str_:
        if char not in op_str:
            op_str = op_str + char

    return op_str


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string))
    print(second_approach(string))
