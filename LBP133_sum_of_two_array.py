########################################################################################################
# Question: sum of two arrays

# Implement a program to find the sum of two arrays and display the result array

# input -------> size and array elements
# con ---------> no
# output ------> print output array

# 4
# 1 2 3 4
# 4 3 2 1

# 5 5 5 5
########################################################################################################
def first_approach(array_1: list, array_2: list) -> list:
    output_array: list = []
    for j in range(len(array_1)):
        op_ele: int = array_1[j] + array_2[j]
        output_array.append(op_ele)
    return output_array


if __name__ == "__main__":
    size_t: int = int(input("Enter the size of array: "))
    first_array: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of the first array: "))
        first_array.append(element)

    print()

    second_array: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of the second array: "))
        second_array.append(element)
    print(f"First Array : {first_array} and Second Array : {second_array}")
    print(first_approach(first_array, second_array))
