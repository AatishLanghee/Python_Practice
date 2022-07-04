########################################################################################################
# Question: Is the String in Order?

# Create a function that takes a string and returns true or false, depending on whether the characters
# are in order or not.

# input -------> a string from the user
# cons --------> for non-empty string print invalid
# output ------> true or false

# abc ------> true
# prakash --> false

# Logic:
# ~~~~~~~
# 1. read a string from the user.
# 2. copy the original string into temp string.
# 3. sort the content of original string.
# 4. compare original and temp string.
# 5. if both are equal then print true else print false.

# Eg:
# s=abc
# t=abc===>abc
# true

# Eg:
# s=prakash
# t=prakash -> aahkprs
# false
########################################################################################################
def first_approach(str_: str,) -> bool:
    threshold: int = ord("a")
    for char in str_.lower():
        if ord(char) < threshold:
            return False
        else:
            threshold = ord(char)
    return True


def second_approach(str_: str,) -> bool:
    temp_str: str = str_
    str_ = list(str_)
    for i in range(len(str_) - 1):
        for j in range(len(str_) - 1):
            if str_[j] > str_[j + 1]:
                str_[j], str_[j + 1] = str_[j+1], str_[j]

    op_str: str = "".join(str_)

    if temp_str != op_str:
        return False

    return True


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string,))
    print(second_approach(string,))
