########################################################################################################
# Question: first non-repeated character

# Program to find first non-repeated character

# input----> a non-empty string from the user
# con -----> no
# output --> non-repeated character

# india ----> n
# indian ---> d

# Logic:
# ~~~~~~
# 1. read a string from the user.
# 2. set unique as true.
# 3. compare each character with remaining all the characters,
# 4. if match found set unique value as false and break
########################################################################################################
def first_approach(string: str, ) -> str:
    for i, char in enumerate(string):
        if char in string[i+1:]:
            continue
        else:
            return char


def second_approach(string: str, ) -> str:
    for i in range(len(string)):
        unique: bool = True
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                unique = False
                break
        if unique:
            return string[i]


if __name__ == "__main__":
    original_string: str = input("Enter the string :")
    print(first_approach(original_string,))
    print(second_approach(original_string,))
