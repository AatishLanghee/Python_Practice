########################################################################################################
# Question:Special Characters

# Program to count number of special characters and white spaces in a given string.

# input --------> A string from the user
# constraint ---> non-empty string
# output -------> number of special characters

# Logic:
# -------
# 1--------------> read a string from the user
# 2 -------------> check each and every character
# 3 -------------> if lower case alphabet, digit, upper case alphabet conitnue
# 4 -------------> else counter++
# 5 -------------> print counter
########################################################################################################
def special_char(string_: str) -> int:
    count: int = 0
    for char in string_:
        if not char.isalnum():
            count = count + 1
    return count


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(special_char(string))
