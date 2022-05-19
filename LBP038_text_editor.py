########################################################################################################
# Question: text editor

# A company launched a new text editor that allows users to enter english letters, numbers and white spaces only.
# If a user attempts to enter any other type of characters, it is counted as miss. Given a String text, write
# an algorithm to help the developer detect the number of misses by a given user in the given input.

# input --------> String
# constraint ---> non-empty string
# output -------> number of misses

# Good@morning! -----> 2

# Logic:
# ~~~~~~~
# 1--------> read a string from the user
# 2 -------> each and every char if it is a special character
# 3 -------> increment counter value
# 4 -------> counter values
########################################################################################################
def count_miss(str_: str) -> int:
    count: int = 0
    for char in str_:
        if char.isalnum():
            continue
        elif char == " ":
            continue
        else:
            count = count + 1

    return count


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(count_miss(string))
