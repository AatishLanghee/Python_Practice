########################################################################################################
# Question: Replace character with its occurrence

# Implement a Program to replace a character with its occurrence in given string.

# input ---------> a string and a character from the user.
# con -----------> non-empty string
# output --------> replaced string

# input: test, t
# output: 1tes2

# Logic:
# ~~~~~~
# 1. read a string s from the user.
# 2. read character ch from the user.
# 3. fetch each character from the string
# 4. if it is ch, print counter
# 5. else print character
########################################################################################################
def first_approach(string: str, required_char: str) -> str:
    op_str: str = ""
    count: int = 1
    for char in string:
        if char == required_char:
            op_str += str(count)
            count += 1
        else:
            op_str += char

    return op_str


if __name__ == "__main__":
    original_string: str = input("Enter the string :")
    required_character: str = input("Enter the required character :")
    print(first_approach(original_string, required_character))
