########################################################################################################
# Question: Sort 0s, 1s and 2s

# sort an array of 0s, 1s and 2s

# Implement a program to read an array and sort array elements with 0s, 1s and 2s.

# input ------> size, array elements
# con --------> size<100
# output -----> print sorted elements
########################################################################################################
def first_approach(array_t: list) -> list:
    for i in range(len(array_t)):
        for j in range(i+1, len(array_t)):
            if array_t[j] < array_t[i]:
                array_t[i], array_t[j] = array_t[j], array_t[i]

    return array_t


if __name__ == "__main__":
    size_t: int = int(input("Enter the size of array: "))
    input_array: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of the array: "))
        input_array.append(element)

    print(f"Input array : {input_array}")
    print(first_approach(input_array,))
