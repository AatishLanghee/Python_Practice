########################################################################################################
# Question: diff between largest and smallest element in array

# Implement a program to read array elements and find the difference between max and min element in an array.

# input -------> size and array elements.
# con ---------> size<100
# output ------> return difference between max and min element.

# 5
# 4 2 5 1 3 ===> 5 - 1 = 4

# Logic=====> a[n-1]-a[1-1]
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
    return sorted_array[-1] - sorted_array[0]


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array, ))
