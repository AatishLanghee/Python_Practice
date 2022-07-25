########################################################################################################
# Question: Increment every element in an array by one unit

# Implement a program to increment every element by one unit in array.

# input ------> size, array elements
# con --------> size<100
# output -----> increment each element by one unit
########################################################################################################
def first_approach(array_t: list) -> list:
    op_array: list = []
    for _ in range(len(array_t)):
        op_array.append(array_t[_] + 1)
    return op_array


if __name__ == "__main__":
    size_t: int = int(input("Enter the size of array: "))
    input_array: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of the array: "))
        input_array.append(element)

    print(f"Input array : {input_array}")
    print(first_approach(input_array,))
