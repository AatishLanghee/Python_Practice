########################################################################################################
# Question: Toggle case

# Implement a program to calculate toggle case of each character of a string

# input -------> A String from user
# constraint --> non-empty String
# output ------> toggle case string

# HeLlO ---> hElLo
#
# Logic:
# ~~~~~~
# 1-------> read a string from the user
# 2 ------> extract every character
# 3 ------> if char is in lower case convert to uppercase & vice versa
# 4 ------> print string
########################################################################################################
def swap_case(str_: str) -> str:
    char: str
    output: list = []
    for char in list(str_):
        if char.isupper():
            char = char.lower()
            output.append(char)
        elif char.islower():
            char = char.upper()
            output.append(char)
    return "".join(output)


def second_approach(str_: str) -> str:
    return str_.swapcase()


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(swap_case(string))
    print(second_approach(string))
