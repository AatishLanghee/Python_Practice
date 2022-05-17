########################################################################################################
# Question: Climbing stairs

# You are climbing a staircase. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# input --------> a number from the user
# constraints --> no
# output -------> number of ways

# Logic:
# ~~~~~
# 1----> 1
# 2 ---> 2
# 3 ---> 3
# 4 ---> 5 and so on..
# fibonacci series
########################################################################################################
def steps(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return steps(n - 1) + steps(n - 2)


if __name__ == '__main__':
    num: int = int(input("Enter the number1: "))
    print(steps(num))
