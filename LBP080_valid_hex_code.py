########################################################################################################
# Question: Valid Hex Code

# Create a function that determines whether a string is a valid hex code.

# A hex code must begin with a pound key # and is exactly 6 characters in length.
# Each character must be a digit from 0-9 or an alphabetic character from A-F.
# All alphabetic characters may be uppercase or lowercase.

# input -----> a string from the user
# con -------> no
# output ----> true or false

#123456 ----> valid
#A1B2C3 ----> valid

#[0-9a-fA-F]{6}

# Logic:
# ~~~~~~
# 1. read a string from the user as s.
# 2. convert each character in the string s into upper case.
# 3. check whether first character is equal to # and the length is 7.
# 	3.1. check each character is in the range or 0-9 or A-F
# 	3.2. if yes print true
# 	3.3. else false
########################################################################################################
def first_approach(str_: str) -> bool:
    if str_[0] != "#" or len(str_) != 7:
        return False

    str_ = str_.lower()

    for i in range(1, len(str_)):

        if (str_[i] > "9" or str_[i] < "0") and (str_[i] > "f" or str_[i] < "a"):
            return False

    return True


def second_approach(str_: str) -> bool:
    import re
    if re.fullmatch("#[0-9a-fA-F]{6}", str_):
        return True

    return False


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string))
    print(second_approach(string))
