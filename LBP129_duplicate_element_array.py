########################################################################################################
# Question: Number of duplicate elements in array

# Implement a program to find the number of duplicate elements present in the given array.

# input ------> size, array elements
# con --------> size<100
# output -----> number of duplicate elements in the array

# 5
# 12 13 14 12 13
# count = 2
########################################################################################################
def first_approach(array_t: list) -> int:
    temp_array: list = array_t.copy()
    count: int = 0
    for i in range(len(temp_array)):
        found: bool = False
        for j in range(i+1, len(temp_array)):
            if temp_array[j] != -1 and temp_array[j] == temp_array[i]:
                if not found:
                    count += 1
                    found = True
                temp_array[j] = -1
    return count


def second_approach(array_t: list) -> int:
    count: int = 0
    count_dict: dict = {}
    for element in array_t:
        if element not in count_dict.keys():
            count_dict[element] = 1
        else:
            count_dict[element] += 1

    for k, v in count_dict.items():
        if v > 1:
            count += 1

    return count


if __name__ == "__main__":
    size_t: int = int(input("Enter the size of array: "))
    input_array: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i + 1} element of the array: "))
        input_array.append(element)

    print(f"Input array : {input_array}")
    print(first_approach(input_array,))
    print(second_approach(input_array,))
