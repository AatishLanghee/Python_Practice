########################################################################################################
# Question: print reverse of each number in an array

# Implement a program to print reverse of each element in an array

# input -----> size and array elements
# con -------> no
# output ----> print reverse of each element in an array

# in: [9, 123, 456, 323]
# out: [9, 321, 654, 323]
########################################################################################################
def reverse(num: int) -> int:
    sum_: int = 0
    while num > 0:
        digit: int = num % 10
        sum_ = sum_ * 10 + digit
        num = num // 10

    return sum_


def first_approach(array_1: list, ) -> list:
    op_array: list = []
    for number in array_1:
        op_array.append(reverse(number))
    return op_array


if __name__ == "__main__":
    size_t: int = int(input("Enter the size of array: "))
    first_array: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of the first array: "))
        first_array.append(element)

    print(f"First Array : {first_array}")
    print(first_approach(first_array,))
