########################################################################################################
# Question: sum of prime numbers in an array

# Implement a program to read an array elements and print sum of all prime elements.

# input -------> size of the array and array elements
# con ---------> size<100
# output ------> sum of all prime elements

# Logic:
# ~~~~~~~
# s=0;
# for(i=0;i<n;i++){
# 	if(isprime(a[i])){
# 		s=s+a[i];
# 	}
# }
########################################################################################################
def is_prime(n: int) -> bool:
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def first_approach(size_t: int) -> int:
    sum_t: int = 0
    for i in range(size_t):
        element: int = int(input(f"Enter the {i+1} element of array :"))
        is_prime_status: bool = is_prime(element)
        if is_prime_status:
            sum_t += element
    return sum_t


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array,))
