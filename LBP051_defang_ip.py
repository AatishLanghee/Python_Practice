########################################################################################################
# Question: Defang an IP address

# Given a valid IP address, return defang version of that IP address.
# Defang IP address replaces every period '.' with "[.]".

# input ----------> A string
# constraint -----> non-empty String
# output ---------> replacement String
#
# 1.1.1.1  ====> 1[.]1[.]1[.]1

# Logic:
# ~~~~~~
# 1------> read a string value from the user
# 2 -----> replace . with [.]
# 3 -----> print the result
########################################################################################################
def first_approach(string: str) -> str:
    op: str = ""
    char: str
    for char in string:
        if char == ".":
            op = op + "[.]"
        else:
            op = op + char
    return op


def second_approach(string: str) -> str:
    return string.replace(".", "[.]")


if __name__ == "__main__":
    ip: str = input("Enter the IP address :")
    print(first_approach(ip))
    print(second_approach(ip))
