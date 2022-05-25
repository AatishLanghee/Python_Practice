########################################################################################################
# Question: Max Occurring Character

# Given a string, implement a program to find max occurring character in the given string

# input -------> A string from the user.
# constraints--> No
# output ------> max occurring character

# welcome ----> e
# java -------> a
########################################################################################################
def first_approach(str_: str) -> None:
    count_dict: dict = {}
    char: str
    for char in str_:
        if char not in count_dict.keys():
            count_dict[char] = 1
        else:
            count_dict[char] = count_dict[char] + 1

    value: int = max(count_dict.values())

    for k, v in count_dict.items():
        if v == value:
            print(k)


def second_approach(str_: str) -> None:
    from collections import Counter
    count_dict: dict = Counter(str_)
    print(max(count_dict, key=count_dict.get))


if __name__ == "__main__":
    str1: str = input("Enter the string :")
    first_approach(str1)
    second_approach(str1)
