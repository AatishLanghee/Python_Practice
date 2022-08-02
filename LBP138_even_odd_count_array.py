########################################################################################################
# Question: number of even and odd elements

# Implement a program to find number of even and odd elements in the given array

# input -------> size and array elements
# con ---------> no
# output ------> print number of even and odd elements line by line
########################################################################################################
from typing import Tuple


def first_approach(array_1: list, ) -> Tuple[int, int]:
    even_count: int = 0
    odd_count: int = 0
    for element_ in array_1:
        if element_ % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count


if __name__ == "__main__":
    size_t: int = int(input("Enter the size of array: "))
    first_array: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of the first array: "))
        first_array.append(element)

    print(f"First Array : {first_array}")
    print(first_approach(first_array,))
