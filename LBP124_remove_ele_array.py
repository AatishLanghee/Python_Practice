########################################################################################################
# Question: delete an element from an array
#
# Implement a program to delete the given element from an array
#
# input -------> size,array elements and element
# con ---------> size<100
# output ------> return array after deleting

# 5
# 1 2 3 4 5
# 3

# 1 2 4 5
########################################################################################################
def first_approach(query: int, array_list_t: list) -> list:
    op_array: list = array_list_t.copy()
    try:
        op_array.remove(query)
        return op_array
    except:
        return op_array


def second_approach(query: int, array_list_t: list) -> list:
    op_list: list = []
    for _ in range(len(array_list_t)):
        if array_list_t[_] != query:
            op_list.append(array_list_t[_])

    return op_list


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    array_list: list = []
    for i in range(size_of_array):
        element: int = int(input(f"Enter the {i + 1} element of array :"))
        array_list.append(element)

    query_element: int = int(input("Enter the query element :"))
    print(first_approach(query_element, array_list,))
    print(second_approach(query_element, array_list,))
