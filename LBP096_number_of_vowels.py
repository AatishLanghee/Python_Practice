########################################################################################################
# Question: Number of vowels

# Implement a program to return number of vowels present in the given string

# input ---------> a string from the user
# con -----------> non-empty string
# output --------> return number of vowels
########################################################################################################
def first_approach(str_: str) -> int:
    count: int = 0
    char: str
    for char in str_.lower():
        if char in "aeiou":
            count += 1

    return count


if __name__ == "__main__":
    string: str = input("Enter a string :")
    print(first_approach(string,))
