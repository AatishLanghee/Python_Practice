########################################################################################################
# Question: max element in an array

# Implement a program to read array elements and find the max element in an array.

# input -------> size and array elements.
# con ---------> size<100
# output ------> return max element

# 5
# 4 2 5 1 3 ===> 5

# Second Approach:

# sort the array in ascending order and get the values as below:
# a[n-1]====>1st max element
# a[n-2]====>2nd max element
# a[n-3]====>3rd max element
########################################################################################################
def first_approach(size_t: int) -> int:
    array_list: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of array :"))
        array_list.append(element)

    max_element: int = -1
    for element in array_list:
        if element > max_element:
            max_element = element

    return max_element


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array, ))
