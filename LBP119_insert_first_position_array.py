########################################################################################################
# Question: inserting element at first position in an array

# Implement a program to insert an element into an array at the first position

# input -------> size,array elements and element to be inserted
# con ---------> size<100
# output ------> return array after insertion
########################################################################################################
def first_approach(size_t: int, array_list_t: list, insert_ele_t: int) -> list:
    op_array: list = [0] * (size_t + 1)
    for i in range(len(op_array) - 1, -1, -1):
        if i == 0:
            op_array[i] = insert_ele_t
        else:
            op_array[i] = array_list_t[i-1]

    return op_array


def second_approach(size_t: int, array_list_t: list, insert_ele_t: int) -> list:
    array_list_t.insert(0, insert_ele)
    return array_list_t


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    array_list: list = []
    for i in range(size_of_array):
        element: int = int(input(f"Enter the {i + 1} element of array :"))
        array_list.append(element)

    insert_ele: int = int(input("Enter the element to insert :"))
    print(first_approach(size_of_array, array_list, insert_ele))
    print(second_approach(size_of_array, array_list, insert_ele))
