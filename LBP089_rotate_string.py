########################################################################################################
# Question: Rotate String

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.

# abcde ===> bcdea,cdeab,deabc,eabcd

# s1=abcde
# s2=deabc
# s3=abcdeabcde

# Logic:
# ~~~~~~
# 1. read strings s1 and s2.
# 2. s3 by adding s1+s1
# 3. s3 contains s2 then return true.
# 4. else false.
########################################################################################################
def first_approach(string: str, req_str: str) -> bool:
    op_list: list = list(string)
    for i in range(len(string)):
        char: str = op_list.pop(0)
        op_list.append(char)
        op_str = "".join(op_list)

        if op_str == req_str:
            return True
    return False


def second_approach(string: str, req_str: str) -> bool:
    if req_str in string + string:
        return True

    return False


if __name__ == "__main__":
    original_string: str = input("Enter the string :")
    required_string: str = input("Enter the required string :")
    print(first_approach(original_string, required_string))
    print(second_approach(original_string, required_string))
