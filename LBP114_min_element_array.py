########################################################################################################
# Question: min element in an array

# Implement a program to read array elements and find the min element in an array.

# input -------> size and array elements.
# con ---------> size<100
# output ------> return min element

# 5
# 4 2 5 1 3 ===> 1

# Second Approach:

# sort the array in ascending order and get the values as below:
# a[3-1] =====>3rd min element
# a[2-1] =====>2nd min element
# a[1-1] =====>1st min element
########################################################################################################
def first_approach(size_t: int) -> int:
    array_list: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of array :"))
        array_list.append(element)

    min_element: int = 100
    for element in array_list:
        if element < min_element:
            min_element = element

    return min_element


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array, ))
