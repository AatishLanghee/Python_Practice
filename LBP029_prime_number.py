########################################################################################################
# Question: Prime Number or Not

# Write a program to check whether the given number is prime number or not.
# A number is said to prime if it is having only two factors. i.e. 1 and number itself.

# input ------> a number from the user
# constraint--> n>1
# output -----> true or false

# Logic:
# ~~~~~~
# n=2 -------> 1,2 -------> true
# n=3 -------> 1,3 -------> true
# n=4 -------> 1,2,4 -----> false
# n=5 -------> 1,5 -------> true
# n=6 -------> 1,2,3,6 ---> false
# and so on..
# n=x -------> 1,2,3,4,5,.....,x ---> if factors==2 then print true else false
########################################################################################################
def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    num: int = int(input("Enter the number1: "))
    print(is_prime(num))
