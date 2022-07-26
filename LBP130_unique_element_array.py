########################################################################################################
# Question: print unique elements in array

# Implement a program to find the unique elements present in the given array.

# input ------> size, array elements
# con --------> size<100
# output -----> print unique elements present in the array

# n=5, 1 1 2 3 4 ====> 1 2 3 4
# n=5, 1 1 1 2 2 ====> 1 2
########################################################################################################
def first_approach(array_t: list) -> list:
    op_list: list = []
    for ele in array_t:
        if ele not in op_list:
            op_list.append(ele)

    return op_list


if __name__ == "__main__":
    size_t: int = int(input("Enter the size of array: "))
    input_array: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of the array: "))
        input_array.append(element)

    print(f"Input array : {input_array}")
    print(first_approach(input_array,))
