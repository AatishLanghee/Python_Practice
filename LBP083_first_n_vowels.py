########################################################################################################
# Question: First N Vowels

# Write a function that returns the first n vowels of a string.

# input ------> a string from the user and an integer value
# cons -------> Return "invalid" if the n exceeds the number of vowels in a string.
# output -----> return first n vowels in the string

# welcome to java, 1 -----> e
# welcome to java, 2 -----> eo
# welcome to java, 3 -----> eoe
# welcome to java, 6 -----> eoeoaa
# welcome to java, 7 -----> invalid

# Logic:
# ~~~~~~
# 1. read a string s from the user and integer as n.
# 2. fetch one by one char from the string s.
# 3. if char == vowel copy that char ch into a new string (ns).
# 4. if n>length of ns then print "invalid" otherwise
# 5. print characters in ns upto n characters.
########################################################################################################
def first_approach(str_: str, num: int) -> str:
    vowels_str: str = ""
    for char in str_:
        if char in ("a", "e", "i", "o", "u"):
            vowels_str += char
    if num > len(vowels_str):
        return "Invalid"

    return vowels_str[:num]


def second_approach(str_: str, num: int) -> str:
    import re
    vowels_str: str = re.sub("[^aeiouAEIOU]", "", str_)

    if num > len(vowels_str):
        return "Invalid"

    return vowels_str[:num]


if __name__ == "__main__":
    string: str = input("Enter the string :")
    number: int = int(input("Enter the number :"))
    print(first_approach(string, number))
    print(second_approach(string, number))
