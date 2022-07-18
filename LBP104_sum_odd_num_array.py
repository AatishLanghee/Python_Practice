########################################################################################################
# Question: sum of odd numbers in an array

# Implement a program to read an array elements and print sum of all odd elements.

# input -------> size of the array and array elements
# con ---------> size<100
# output ------> sum of all odd elements

# Logic:
# ~~~~~~~
# s=0;
# for(i=0;i<n;i++){
#
# 	if(a[i]%2!=0){
#
# 		s=s+a[i];
# 	}
#
# }
########################################################################################################
def first_approach(size_t: int) -> int:
    sum_t: int = 0
    for i in range(size_t):
        element: int = int(input(f"Enter the {i+1} element of array :"))
        if (element % 2) == 1:
            sum_t += element
    return sum_t


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array,))
