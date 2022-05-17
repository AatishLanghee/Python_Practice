########################################################################################################
# Question: Valid Palindrome

# Given a string, determine if it is a Palindrome string or not.
# A String is Palindrome if it is equal to reverse of the original string.

# input ------> A String from the user
# constraint--> Non-empty String
# output -----> Palindrome or not

# Logic:
# ~~~~~~
# 1. read a string from the user
# 2. reverse the original string and store it in a temp variable.
# 3. compare original str and temp str, if both are equal then pali else not.
########################################################################################################
def string_palindrome(string_: str) -> str:
    start_: int = 0
    end_: int = len(string_) - 1

    while start_ < end_:
        if string_[start_] != string_[end_]:
            return "Not Palindrome"
        start_ = start_ + 1
        end_ = end_ - 1

    return "Palindrome"


if __name__ == '__main__':
    string: str = input("Enter the string: ")
    print(string_palindrome(string))
