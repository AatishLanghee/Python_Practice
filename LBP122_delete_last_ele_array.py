########################################################################################################
# Question: delete an element from last location in an array

# Implement a program to delete an element from an array at the last position

# input -------> size,array elements
# con ---------> size<100
# output ------> return array after deleting from last location

# 5
# 1 2 3 4 5

# 1 2 3 4
########################################################################################################
def first_approach(array_list_t: list) -> list:
    return array_list_t[:-1]


def second_approach(array_list_t: list,) -> list:
    op_list: list = []
    for _ in range(len(array_list_t) - 1):
        op_list.append(array_list_t[_])

    return op_list


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    array_list: list = []
    for i in range(size_of_array):
        element: int = int(input(f"Enter the {i + 1} element of array :"))
        array_list.append(element)

    print(first_approach(array_list,))
    print(second_approach(array_list,))
