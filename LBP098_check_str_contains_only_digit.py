########################################################################################################
# Question: Check only digits

# Implement a program to check if a string contains only digits.

# input ----> a string from the user
# con ------> no
# output ---> Yes or No
########################################################################################################
def first_approach(str_: str) -> str:
    char: str
    for char in str_.lower():
        if char not in "0123456789":
            return "No"

    return "Yes"


if __name__ == "__main__":
    string: str = input("Enter a string :")
    print(first_approach(string,))
