########################################################################################################
# Question: Print all permutations of a string

# Given a string str, the task is to print all the permutations of str.
# A permutation is an arrangement of all or part of a set of objects, with regard to the order of the arrangement.
# For instance, the words ‘bat’ and ‘tab’ represents two distinct permutation (or arrangements) of a similar
# three-letter word.

# input ----> string from the user
# con ------> no
# output ---> all permutations of the string

# A (1!=1)  ----> A
# AB(2!=2)   ---> AB BA
# ABC(3!=6)  ---> ABC ACB BAC BCA CAB CBA

# Learn Backtracking**
########################################################################################################
def permutation_calculation(str__: list, start_, end_, op_list_: list) -> None:
    if start_ == end_:
        op_list_.append("".join(str__))
    else:
        for i in range(start_, len(str__)):
            str__[start_], str__[i] = str__[i], str__[start_]
            permutation_calculation(str__, start_ + 1, end_, op_list_)
            str__[start_], str__[i] = str__[i], str__[start_]


def first_approach(str_: str) -> list:
    op_list = []
    start: int = 0
    end: int = len(str_) - 1
    permutation_calculation(list(str_), start, end, op_list)
    return op_list


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string))
