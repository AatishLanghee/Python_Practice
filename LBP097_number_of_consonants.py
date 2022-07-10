########################################################################################################
# Question: Number of consonants

# Implement a program to return number of consonants present in the given string

# input ---------> a string from the user
# con -----------> non-empty string
# output --------> return number of consonants
########################################################################################################
def first_approach(str_: str) -> int:
    count: int = 0
    char: str
    for char in str_.lower():
        if char not in "aeiou":
            count += 1

    return count


if __name__ == "__main__":
    string: str = input("Enter a string :")
    print(first_approach(string,))
