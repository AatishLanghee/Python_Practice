########################################################################################################
# Question: number of occurrences of an element

# Implement a program to find the number of occurrences of the given element.

# input -------> size,array element and key element
# con ---------> size<100
# output ------> return number of occurrences

# Logic:
# ~~~~~~~~
# for(each element in array)
# {
# 	if element == key
# 	counter++;
# }
#
# print counter;
########################################################################################################
def first_approach(size_t: int) -> int:
    array_list: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of array :"))
        array_list.append(element)

    key_search: int = int(input("Enter the key to search :"))
    count: int = 0

    for element in array_list:
        if element == key_search:
            count += 1
    return count


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array, ))
