########################################################################################################
# Question: X's and O's, Nobody knows

# Create a function that takes a string,
# check if it has the same number of x's and o's and returns either true or false.

# Rules:

# 1. return boolean value true or false.
# 2. returns true if the amount x's and o's are the same.
# 3. returns false if they are not the same amount.
# 4. the string can contain any character.
# 5. when 'x' and 'o' are not in the string, return true.

# input ---------> a string
# constraints----> no
# output --------> true or false
########################################################################################################
def first_approach(string_: str) -> bool:
    x_count: int = 0
    o_count: int = 0
    char: str
    for char in string_.lower():
        if char == 'x':
            x_count += 1
        elif char == 'o':
            o_count += 1

    if x_count == o_count or (x_count == 0 and o_count == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    string: str = input("Enter a string :")
    print(first_approach(string))
