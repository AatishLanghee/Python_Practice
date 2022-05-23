########################################################################################################
# Question: Jewels and Stones

# You are given two Strings, one is jewels representing the types of stones that are jewels, and other is stones
# representing the stones you have. Each character in stones is a type of stone you have,
# you want to know how many of the stones you have are also jewels.

# Letter are case-sensitive. so "a" is considered as a different type of stone from "A".

# input ------> A string
# constraint -> no
# output -----> how many of the stones

# Jewels="aA"
# Stones="aAAbbbb"
# 1+2=3

# Logic:
# ~~~~~~
# 1 -------> read the values of J and S
# 2 -------> read every char from J and check whether it is in S or not.
# 3 -------> if it is available, then increment the counter
# 4 -------> print counter
########################################################################################################
def first_approach(jw: str, st: str) -> int:
    count: int = 0
    for j_ in jw:
        for s_ in st:
            if s_ == j_:
                count = count + 1

    return count


def second_approach(jw: str, st: str) -> int:
    count: int = 0
    for j_ in jw:
        count = count + st.count(j_)
    return count


if __name__ == "__main__":
    j: str = input("Enter the jewels :")
    s: str = input("Enter the stones :")
    print(first_approach(j, s))
    print(second_approach(j, s))
