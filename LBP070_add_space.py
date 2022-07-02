########################################################################################################
# Question: Space between each character

# Create a function that takes a string and returns a string with spaces in between all the characters.

# input ------------> a string
# constraints-------> No
# output -----------> string

# java -----> j a v a
# prakash --> p r a k a s h
# python ---> p y t h o n

# Logic:
# ~~~~~~
# 1. read a string from the user as s
# 2. fetch each character ch from s.
# 3. print ch followed by space.
########################################################################################################
def first_approach(str_: str) -> str:
    op_: str = ""
    for char in str_.lower():
        op_ = op_ + char + " "

    return op_


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string))
