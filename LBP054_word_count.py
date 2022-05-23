########################################################################################################
# Question: Get word count

# Create a function/method that takes a string and return the word count.
# The string will be a sentence.

# Input: A string
# Constraints: No
# Output: Word count

# Logic:
# ~~~~~~~
# 1. read a string from the user.
# 2. repeat a loop and search for spaces, counter++
# 3. print counter+1 ---> number of words in the given string.
########################################################################################################
def word_count(string_: str) -> int:
    op_list: list = string_.split(" ")
    return len(op_list)


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(word_count(string))
