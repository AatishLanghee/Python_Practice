########################################################################################################
# Question: sum of all elements in array

# Implement a program to read an array elements and print sum of all its elements.

# input -------> size of the array and array elements
# con ---------> size<100
# output ------> sum of all elements

# logic:
# ~~~~~~
# s=0
# for(i=0;i<n;i++){
# s=s+a[i];
# }
########################################################################################################
def first_approach(size_t: int) -> int:
    sum_t: int = 0
    for i in range(size_t):
        element: int = int(input(f"Enter the {i+1} element of array :"))
        sum_t += element
    return sum_t


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array,))
