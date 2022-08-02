########################################################################################################
# Question: sum of first and last, second and second last and so on

# Implement a program to find the sum of first and last, second and second last and so on in an array.

# input -----> size and array elements
# con -------> no
# output ----> print sum of first and last, second and second last and so on

# 1,2,3,4,5
# 6,6,6

# 1,2,3,4,5,6
# 7,7,7
########################################################################################################
def first_approach(array_1: list, ) -> list:
    start: int = 0
    end: int = len(array_1) - 1
    op_array: list = []
    while start <= end:
        sum_: int = array_1[start] + array_1[end]
        op_array.append(sum_)
        start += 1
        end -= 1

    return op_array


if __name__ == "__main__":
    size_t: int = int(input("Enter the size of array: "))
    first_array: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of the first array: "))
        first_array.append(element)

    print(f"First Array : {first_array}")
    print(first_approach(first_array,))
