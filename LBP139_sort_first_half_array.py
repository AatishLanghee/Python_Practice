########################################################################################################
# Question: Sort only First half of the array

# Implement a program to reverse only first half of the array and keep remaining elements as original.

# input ------> size and array elements
# con --------> no
# output -----> reverse only first half of the array

# input:
# 5
# 2 0 1 4 5

# Output
# 0 1 2 4 5
########################################################################################################
def sort(temp: list) -> list:
    for x in range(len(temp)):
        for y in range(x+1, len(temp)):
            if temp[x] > temp[y]:
                temp[x], temp[y] = temp[y], temp[x]

    return temp


def first_approach(array_1: list, ) -> list:
    mid: int = len(array_1) // 2

    if len(array_1) % 2 == 1:
        mid += 1

    op_array: list = []

    sorted_array: list = sort(array_1[0:mid])

    for data in sorted_array:
        op_array.append(data)

    for j in range(mid, len(array_1)):
        op_array.append(array_1[j])

    return op_array


if __name__ == "__main__":
    size_t: int = int(input("Enter the size of array: "))
    first_array: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of the first array: "))
        first_array.append(element)

    print(f"First Array : {first_array}")
    print(first_approach(first_array,))
