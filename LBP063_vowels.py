########################################################################################################
# Question: How many vowels

# Create a function that takes a string and returns the number of vowels contained within it.

# input -----------> a string
# constraint ------> no
# output ----------> number of vowels

# Logic:
# ~~~~~~
# 1. read a string from the user
# 2. fetch each character and check whether it is equal to 'a' or 'e' or 'i' or 'o' or 'u' then counter++
# 3. print counter.
########################################################################################################
def solution(string_: str) -> int:
    counter: int = 0
    char: string
    for char in string_.lower():
        if char in ("a", "e", "i", "o", "u"):
            counter += 1
    return counter


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(solution(string))
