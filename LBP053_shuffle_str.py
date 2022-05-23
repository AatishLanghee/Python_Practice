########################################################################################################
# Question: Shuffle String

# Given a string s, and an integer array indices of the same length.
# The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string,
# return shuffled string.

# input ---------> a string and an array
# constraint ----> no
# output --------> a string

# s=art
#   012

# a=1 0 2 = r a t
#   0 1 2

# ts=0=>r 1=>a 2=>t

# Eg:
# aiohn
# 31420

# nihao

# Logic:
# ~~~~~~
# 1------------> read a string
# 2------------> read an array with indices
# 3------------> create an array with the following formula ===> ts[a[i]]=s[i]
#
# ts[a[i]]=s[i]
#
# ts[a[0]]=s[0] ====> ts[1]=s[0]====>ts[1]=a
# ts[a[1]]=s[1] ====> ts[0]=s[1]====>ts[0]=r
# ts[a[2]]=s[2] ====> ts[2]=s[2]====>ts[2]=t
#
# ts[0],ts[1],ts[2] ===> rat
########################################################################################################
def shuffle_string(string_: str, array_: list) -> str:
    # Initialize op_list to some value (here, 0) of same number of elements as string length
    # because empty list will give list index out of range error
    op_list: list = [0] * len(string_)
    for j in range(len(string_)):
        op_list[array_[j]] = string_[j]
    return "".join(op_list)


if __name__ == "__main__":
    string: str = input("Enter the string :")
    array: list = []
    for i in range(len(string)):
        data: int = int(input(f"Enter the {i} element of array:"))
        array.append(data)
    print(shuffle_string(string, array))
