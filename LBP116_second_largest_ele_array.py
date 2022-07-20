########################################################################################################
# Question: second largest element in an array

# Implement a program to read array elements and find the second max element in an array.

# input -------> size and array elements.
# con ---------> size<100
# output ------> return second max element in array

# Logic=====> a[n-2]
########################################################################################################
def sort_array(array: list) -> list:
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array


def first_approach(size_t: int) -> int:
    array_list: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of array :"))
        array_list.append(element)

    sorted_array: list = sort_array(array_list)
    return sorted_array[-2]


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array, ))
