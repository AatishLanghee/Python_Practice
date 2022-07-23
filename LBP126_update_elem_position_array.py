########################################################################################################
# Question: update an element in an array

# Implement a program to update an element in the given array based on position

# input ------> size,array elements and element to be updated and location
# con---------> size<100
# output -----> return array after updating

# Eg:
# 5
# 11 22 77 88 10
# 1
# 99

# output: 11 99 77 88 10
########################################################################################################
def first_approach(array: list, pos: int, n_e: int) -> list:
    op_list: list = []
    for _ in range(len(array)):
        if _ == pos:
            op_list.append(n_e)
        else:
            op_list.append(array[_])

    return op_list


if __name__ == "__main__":
    size_array: int = int(input("Enter the size of an array :"))
    input_array: list = []
    for i in range(size_array):
        element: int = int(input(f"Enter the {i + 1} element of the array :"))
        input_array.append(element)

    print("input_array :", input_array)
    position: int = int(input(f"Enter the position of element to update :"))
    new_element: int = int(input(f"Enter the new element to update :"))
    print(first_approach(input_array, position, new_element))
