########################################################################################################
# Question: sum of strong numbers in an array

# Implement a program to read an array elements and print sum of all strong numbers in array.

# input -------> size of the array and array elements
# con ---------> size<100
# output ------> sum of all strong numbers

# 145 = 1!+4!+5!=1+24+120=145 ----> strong number

# Logic:
# ~~~~~~
# int fact(int n){
# }

# int isStrong(int n){
# }

# s=0;
# for(i=0;i<n;i++){
#
# 	if(isStrong(a[i])){
# 	s=s+a[i];
# 	}
# }
########################################################################################################
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def is_strong_number(n: int) -> bool:
    original_num: int = n
    output_num: int = 0
    while n > 0:
        digit: int = n % 10
        fact: int = factorial(digit)
        output_num += fact
        n = n // 10

    if original_num != output_num:
        return False

    return True


def first_approach(size_t: int) -> int:
    sum_t: int = 0
    for i in range(size_t):
        element: int = int(input(f"Enter the {i+1} element of array :"))
        is_strong_status: bool = is_strong_number(element)
        if is_strong_status:
            sum_t += element
    return sum_t


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array,))
