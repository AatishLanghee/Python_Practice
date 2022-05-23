########################################################################################################
# Question: Reverse the order of a String

# create a method/function that takes a string as its argument and returns the string in reversed order.

# input ---------> a string
# constraint ----> no
# output --------> reversed string

# Hello ----------> olleH
# Hello World ----> olleH dlroW

# Logic:
# ~~~~~~~
# 1. read s
# 2. print each character from end to begin
########################################################################################################
def reverse_str(string_: str) -> str:
    op_list: list = []
    for i in range(len(string_), 0, -1):
        op_list.append(string_[i - 1])
    return "".join(op_list)


def first_approach(string_1: str) -> str:
    op_list: list = []
    data = string_1.split(" ")
    for d in data:
        op_list.append(reverse_str(d))
    return " ".join(op_list)


def second_approach(string_1: str) -> str:
    op_list: list = []
    data = string_1.split(" ")
    for d in data:
        op_list.append(d[::-1])
    return " ".join(op_list)


if __name__ == "__main__":
    str1: str = input("Enter the string :")
    print(first_approach(str1))
    print(second_approach(str1))
