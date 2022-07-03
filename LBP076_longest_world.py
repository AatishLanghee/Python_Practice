########################################################################################################
# Question: Longest Word

# Write a function that finds the longest word in a sentence.
# If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period (and the like) count as part of the word
# (e.g. O'Connor is 8 characters long).

# input ------> a string from the user
# con --------> no
# output------> longest word

# C C++ JAVA AND PYTHON =====> PYTHON
# 1  3    4   3    6

# case1:
# prakash sir classes are very good ====> prakash
#    7     3      7   3    4    4

# case2:
# prakash sir classes are very good ====> classes (based on asc value of first character) Need to try
#    7     3      7   3    4    4

# Logic:
# ~~~~~~
# 1. read a sentence as s from the user.
# 2. fetch words as tokens from the string.
# 3. fetch each token and compare with remaining tokens w.r.t length.
# 4. print longest word.
########################################################################################################
def first_approach(str_: str) -> str:
    string_lst = str_.split(" ")
    longest_string = None
    max_len = -1
    for word in string_lst:
        if len(word) > max_len:
            max_len = len(word)
            longest_string = word

    return longest_string


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string))
