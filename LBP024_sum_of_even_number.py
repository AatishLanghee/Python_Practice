########################################################################################################
# Question: Sum of even numbers

# Implement a program to find sum of even number between x and y both are inclusive.

# input -----> two int values
# constraint-> no
# output ----> sum of even numbers between x and y

# Logic:
# ------
# 1 ----> read x & y values from the user
# 2 ----> repeat a loop from x to y both are inclusive (<=) [exclusive<]
# 3 ----> check every number if it is even then add to sum
# 4 ----> return sum
########################################################################################################
def sum_of_even_num(num1_: int, num2_: int) -> int:
    sum_: int = 0
    for number in range(num1_, num2_+1):
        if number % 2 == 0:
            sum_ = sum_ + number
    return sum_


if __name__ == '__main__':
    num1: int = int(input("Enter the number1: "))
    num2: int = int(input("Enter the number2: "))
    print(sum_of_even_num(num1, num2))
