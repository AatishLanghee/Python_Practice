########################################################################################################
# Question: sum of elements in an array ending with 3

# Implement a program to read an array elements and print sum of elements ending with 3 in array.

# input -------> size of the array and array elements
# con ---------> size<100
# output ------> sum of elements ending with 3

# Logic:
# ~~~~~~
# s=0
# for(i=0;i<n;i++){
#
# 	if(a[i]%10==3){
# 	s=s+a[i];
# 	}
# }
########################################################################################################
def ending_with_3(n: int) -> bool:
    last_digit: int = n % 10
    if last_digit == 3:
        return True
    return False


def first_approach(size_t: int) -> int:
    sum_t: int = 0
    for i in range(size_t):
        element: int = int(input(f"Enter the {i+1} element of array :"))
        is_strong_status: bool = ending_with_3(element)
        if is_strong_status:
            sum_t += element
    return sum_t


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array,))
