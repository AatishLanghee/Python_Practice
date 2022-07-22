########################################################################################################
# Question: delete an element from an array at the given location

# Implement a program to delete an element from an array at the position

# input -------> size,array elements and position
# con ---------> size<100
# output ------> return array after deleting from the location

# 5
# 1 2 3 4 5
# 3

# 1 2 3 5
########################################################################################################
def first_approach(array_list_t: list, position_t: int) -> list:
    op_list: list = array_list_t.copy()
    op_list.pop(position_t)
    return op_list


def second_approach(array_list_t: list, position_t: int) -> list:
    op_list: list = []
    for _ in range(len(array_list_t)):
        if _ != position_t:
            op_list.append(array_list_t[_])

    return op_list


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    array_list: list = []
    for i in range(size_of_array):
        element: int = int(input(f"Enter the {i + 1} element of array :"))
        array_list.append(element)

    position: int = int(input("Enter the position of the element :"))
    print(first_approach(array_list, position))
    print(second_approach(array_list, position))
