########################################################################################################
# Question: Sum of digits between two numbers

# Create a function that sums the total number of digits between two numbers inclusive.
# for example, if the numbers are 19 and 22, then (1+9)+(2+0)+(2+1)+(2+2)=19.

# input ----------> two numbers from the user
# constraints ----> no
# output ---------> sum of digits between n1 and n2

# Logic:
# ~~~~~~
# 1 -----------> read n1 and n2
# 2 -----------> run a loop fron n1 to n2
# 3 -----------> cal sum of digits between the number n1 and n2 and store result in s
# 4 -----------> print sum
########################################################################################################
def digit_sum(n: int) -> int:
    sum_: int = 0
    while n != 0:
        digit: int = n % 10
        sum_ = sum_ + digit
        n = n // 10
    return sum_


def final_sum(n1: int, n2: int) -> int:
    sum_: int = 0
    for num in range(n1, n2 + 1):
        sum_ = sum_ + digit_sum(num)
    return sum_


if __name__ == "__main__":
    num1: int = int(input("Enter the first num :"))
    num2: int = int(input("Enter the second num :"))
    print(final_sum(num1, num2))
