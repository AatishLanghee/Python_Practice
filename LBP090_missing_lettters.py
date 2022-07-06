########################################################################################################
# Question: Missing Letters
#
# Given a string containing unique letters, return a sorted string with the letters that don't appear in the string.
#
# input ---------> a string from the user
# con -----------> no
# output --------> return missing characters
#
# abc -----> defghijklmnopqrstuvwxyz
########################################################################################################
def first_approach(string: str, ) -> str:
    alpha_string: str = "abcdefghijklmnopqrstuvwxyz"
    op_str: str = ""
    string_lst: list = list(string)
    for char in alpha_string:
        if char in string_lst:
            string_lst.remove(char)
        else:
            op_str += char

    return op_str


if __name__ == "__main__":
    original_string: str = input("Enter the string :")
    print(first_approach(original_string,))
