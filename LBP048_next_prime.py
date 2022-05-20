########################################################################################################
# Question: Next Prime

# Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.

# input ----------> a number
# constraint -----> prime number
# output ---------> prime number

# 10---->11
# 11---->11
# 14---->17 etc
#
# Logic:
# ~~~~~~
# 1. read a number 'n' from the user.
# 2. run a looping statement
# 	for i starts from 'n' and run an infinite loop
# 	100 -----> ..............x stop (break)
# 3. check every number if it is a prime then return.
# 4. else repeat
########################################################################################################
def cal_prime(num_: int) -> bool:
    for i in range(2, num_):
        if num_ % i == 0:
            return False
    return True


def next_prime(num_: int) -> int:
    while not (cal_prime(num_)):
        num_ = num_ + 1
    return num_


if __name__ == "__main__":
    num: int = int(input("Enter the number :"))
    print(next_prime(num))
