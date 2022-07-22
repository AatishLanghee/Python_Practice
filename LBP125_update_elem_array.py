########################################################################################################
# Question: update an element in an array

# Implement a program to update an element in the given array

# input ------> size,array elements and element to be updated (old element & new element)
# con---------> size<100
# output -----> return array after updating

# Eg:
# 5
# 1 2 3 4 5
# 3
# 9

# output: 1 2 9 4 5
########################################################################################################
def first_approach(array: list, o_e: int, n_e: int) -> list:
    op_list: list = []
    for data in array:
        if data != o_e:
            op_list.append(data)
        else:
            op_list.append(n_e)

    return op_list


if __name__ == "__main__":
    size_array: int = int(input("Enter the size of an array :"))
    input_array: list = []
    for i in range(size_array):
        element: int = int(input(f"Enter the {i + 1} element of the array :"))
        input_array.append(element)

    print("input_array :", input_array)
    old_element: int = int(input(f"Enter the element from the array to update :"))
    new_element: int = int(input(f"Enter the new element to update :"))
    print(first_approach(input_array, old_element, new_element))
