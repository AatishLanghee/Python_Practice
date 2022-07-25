########################################################################################################
# Question: array reverse

# Write a program to reverse the elements present in an array

# input ------> size, array elements
# con --------> size<100
# output -----> return array in reverse

# Eg:

# 5
# 1 2 3 4 5

# output: 5 4 3 2 1
########################################################################################################
def first_approach(array_t: list) -> list:
    op_array: list = []
    for _ in range(len(array_t) - 1, -1, -1):
        op_array.append(array_t[_])

    return op_array


def second_approach(array_t : list) -> list:
    return array_t[::-1]


if __name__ == "__main__":
    size_t: int = int(input("Enter the size of array: "))
    input_array: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of the array: "))
        input_array.append(element)

    print(f"Input array : {input_array}")
    print(first_approach(input_array,))
    print(second_approach(input_array,))
