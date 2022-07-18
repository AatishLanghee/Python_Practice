########################################################################################################
# Question: reading and writing an array

# Implement a program to read an array elements and write on the screen.

# input -------> size of the array and array elements
# con ---------> size<100
# output ------> the given array

# Inputs:
# size of array: 5
# Array elements: 7 5 3 1 9

# Output: 7 5 3 1 9

# array: it is a collection of similar type of data elements (int)
# array index starts from 0 to size-1

# n
# for(i=0;i<n;i++)
# for(i=1;i<=n;i++)
########################################################################################################
def first_approach(size_t: int) -> list:
    op_list: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i+1} element of array :"))
        op_list.append(element)
    return op_list


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array,))
