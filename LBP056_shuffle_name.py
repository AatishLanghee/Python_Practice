########################################################################################################
# Question: Shuffle the Name

# Create a function/method that accepts a string (of person’s first and last name) and
# returns a string with in first and last name swapped).

# Input:  two space separated strings
# Constraints: No
# Output: return last name followed by first name

# Prakash Babu -----> Babu Prakash

# Logic:
# ~~~~~~
# 1. read s1
# 2. read s2
# 3. print s2 s1
########################################################################################################
def first_approach(string_1: str) -> str:
    return " ".join(string_1.split(" ")[::-1])


def second_approach(string_1: str) -> str:
    op_: list = string_1.split(" ")
    return op_[1] + " " + op_[0]


if __name__ == "__main__":
    str1: str = input("Enter the string :")
    print(first_approach(str1))
    print(second_approach(str1))
