########################################################################################################
# Question: sum of elements available at even index

# Implement a program to find the sum of elements available at even index locations in an array.

# input ----> size and array elements
# con ------> no
# output ---> print sum value

# 5
# 1 2 3 4 5
# 0 1 2 3 4 ====> 0,2,4 ===> 1+3+5=9
########################################################################################################
def first_approach(array_1: list, ) -> int:
    sum_: int = 0
    for j in range(len(array_1)):
        if j % 2 == 0:
            sum_ += array_1[j]
    return sum_


if __name__ == "__main__":
    size_t: int = int(input("Enter the size of array: "))
    first_array: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of the first array: "))
        first_array.append(element)

    print(f"First Array : {first_array}")
    print(first_approach(first_array, ))
