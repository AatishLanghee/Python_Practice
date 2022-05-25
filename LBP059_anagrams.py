########################################################################################################
# Question: Anagrams

# Two strings a and b are called anagrams, if they contain all the same characters in the same frequencies.

# input --------> two strings a and b
# constraint ---> no
# output -------> true or false

# abcd,dabc -----> anagrams
# abcd,dabb -----> not anagrams
# listen,silent -> anagrams
#
# Logic:
# ~~~~~~
# 1. read s1
# 2. read s2
# 3. sort string s1 ----> abcd
# 4. sort string s2 ----> abcd
# 5. compare s1 and s2 if both are equal print true else false
########################################################################################################
def sort_string(str_: str) -> str:
    str_ = list(str_)
    for i in range(len(str_)):
        for j in range(i+1, len(str_)):
            if str_[i] > str_[j]:
                str_[i], str_[j] = str_[j], str_[i]
    return "".join(str_)


def first_approach(str1_: str, str2_: str) -> bool:
    if sort_string(str1_) == sort_string(str2_):
        return True
    return False


def second_approach(str1_: str, str2_: str) -> bool:
    if sorted(str1_) == sorted(str2_):
        return True
    return False


if __name__ == "__main__":
    str1: str = input("Enter the first string :")
    str2: str = input("Enter the second string :")
    print(first_approach(str1, str2))
    print(second_approach(str1, str2))
