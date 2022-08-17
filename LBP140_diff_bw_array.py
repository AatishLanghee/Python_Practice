########################################################################################################
# Question: Difference between two arrays

# Implement a program to find the difference between two arrays

# input -------> size and array elements
# con ---------> no
# output ------> print difference between two arrays as third array

# input:
# 5
# 1 2 3 4 5
# 5 4 3 2 1

# Output
# -4 -2 0 2 4
########################################################################################################

def solution(arr_1: list, arr_2: list) -> list:
    op_array: list = []
    for _ in range(len(arr_1)):
        op_ele: int = arr_1[_] - arr_2[_]
        op_array.append(op_ele)

    return op_array


if __name__ == "__main__":
    size_t: int = int(input("Enter the size of the array :"))
    first_array: list = []
    for i in range(size_t):
        ele: int = int(input(f"Enter the {i+1} element of the first array :"))
        first_array.append(ele)

    print()

    second_array: list = []
    for j in range(size_t):
        ele_: int = int(input(f"Enter the {j + 1} element of the second array :"))
        second_array.append(ele_)

    print(f"First Array : {first_array} and second array :{second_array}")
    print(solution(first_array, second_array))
