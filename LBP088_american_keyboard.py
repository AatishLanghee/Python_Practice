########################################################################################################
# Question: American keyboard

# Given a string, return the true if that can be typed using letters of alphabet on only
# one row's of American keyboard like the image below.
# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# Note:
# 1. You may use one character in the keyboard more than once.
# 2. You may assume the input string will only contain letters of alphabet.

# input -------> a string from the user
# cons  -------> no
# output ------> true or false

# Logic:
# ~~~~~~
# 1. read a string s from the user.
# 2. assign r1 = "qwertyuiop"
# 3. assign r2 = "asdfghjkl"
# 4. assign r3 = "zxcvbnm"
# 5. fetch char by char from original string s.
# 6. if it is present in r1 or r2 or r3 increment c1,c2 and c3
# 7. c1==len(s1) or c2==len(s2) or c3=len(s3) then print true else print false
########################################################################################################
def first_approach(string: str) -> bool:

    first_row: str = "qwertyuiop"
    second_row: str = "asdfghjkl"
    third_row: str = "zxcvbnm"
    final_string: str = ""
    for i, char in enumerate(string):
        if i == 0:
            if char in first_row:
                final_string = first_row
            elif char in second_row:
                final_string = second_row
            else:
                final_string = third_row
        else:
            if char in final_string:
                continue
            else:
                return False

    return True


def second_approach(string: str) -> bool:
    first_row: str = "qwertyuiop"
    second_row: str = "asdfghjkl"
    third_row: str = "zxcvbnm"
    c1, c2, c3 = 0, 0, 0
    for i in string:
        if i in first_row:
            c1 = c1 + 1
        if i in second_row:
            c2 = c2 + 1
        if i in third_row:
            c3 = c3 + 1
    if c1 == len(string) or c2 == len(string) or c3 == len(string):
        return True
    else:
        return False


if __name__ == "__main__":
    original_string: str = input("Enter the string :")
    print(first_approach(original_string, ))
    print(second_approach(original_string, ))
