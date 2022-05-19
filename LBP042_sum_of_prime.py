########################################################################################################
# Question: Sum of prime numbers

# Jackson, a math student, is developing an application on prime numbers. for the given two integers on the display
# of the application, the user has to identify all the prime numbers within the given range
# (including the given values). Afterwards the application will sum all those prime numbers.
# Jackson has to write an algorithm to find the sum of all the prime numbers of the given range.
# Write an algorithm to find the sum of all the prime numbers of the given range.

# input -----> two space separated integers RL and RR.
# output ----> sum of the prime numbers between RL and RR.

# Logic:
# ~~~~~~
# 1------------> read x and y
# 2 -----------> check each number inbetween x and y
# 3 -----------> if it is a prime then add it into sum
# 4 -----------> print sum
########################################################################################################
def calculate_prime(num: int) -> bool:
    count: int = 0
    for i in range(1, num+1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        return True
    else:
        return False


def app(n1: int, n2: int) -> int:
    sum_: int = 0
    result: bool
    for num in range(n1, n2 + 1):
        result = calculate_prime(num)
        if result:
            sum_ = sum_ + num

    return sum_


if __name__ == "__main__":
    num1: str
    num2: str
    num1, num2 = input("Enter the two number separated by space :").split()
    print(app(int(num1), int(num2)))
