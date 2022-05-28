########################################################################################################
# Question: Find the Bomb

# Write a function that finds the word "bomb" in the given string (not case sensitive) return "DUCK!" if found,
# else return "Relax there's no bomb."

# input ---------> a string
# constraint ----> no
# output --------> "DUCK!" or "Relax, There's no bomb."

# Logic:
# ~~~~~~~
# 1. read a string from the user.
# 2. convert the string into lowercase.
# 3. search for bomb word in the string.
# 4. if result is true then print "DUCK!".
# 5. if result is not found then print "Relax, There's no bomb."
########################################################################################################
def first_approach(string: str) -> str:
    if "bomb" in string.lower():
        return "DUCK!"
    else:
        return "Relax there's no bomb."


def second_approach(string: str) -> str:
    test_string: str = "bomb"
    for i in range(len(string)):
        for j in range(len(test_string)):
            if i < len(string) and string[i] == test_string[j]:
                i = i + 1
            else:
                break

            if j == len(test_string) - 1:
                return "DUCK!"
    return "Relax there's no bomb."


if __name__ == "__main__":
    string_: str = input("Enter the string :")
    print(first_approach(string_))
    print(second_approach(string_))
