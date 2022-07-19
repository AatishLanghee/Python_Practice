########################################################################################################
# Question: sum of palindrome numbers in an array

# Implement a program to read an array elements and print sum of all palindrome numbers in array.

# input -------> size of the array and array elements
# con ---------> size<100
# output ------> sum of all palindrome numbers

# Logic:
# ~~~~~~
# int isPali() ----> 1 or 0
# s=0;
# for(i=0;i<n;i++){
# 	if(isPali(a[i])){
# 		s=s+a[i];
# 	}
# }
########################################################################################################
def is_palindrome(n: int) -> bool:
    result_num: int = 0
    original_num: int = n

    while n > 0:
        digit: int = n % 10
        result_num = result_num * 10 + digit
        n = n // 10

    if result_num != original_num:
        return False
    return True


def first_approach(size_t: int) -> int:
    sum_t: int = 0
    for i in range(size_t):
        element: int = int(input(f"Enter the {i+1} element of array :"))
        is_prime_status: bool = is_palindrome(element)
        if is_prime_status:
            sum_t += element
    return sum_t


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array,))
