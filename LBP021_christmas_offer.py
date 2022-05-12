########################################################################################################
# Question: Christmas Offer

# An e-commerce company plans to give their customers a special discount for the Christmas, they are planning to
# offer a flat discount. The discount value is calculated as the sum of all prime digits in the total bill amount.

# Write an algorithm to find the discount value for the given total bill amount.

# input ----> the input consists of an integer order value representing the total bill amount
# condition-> no conditions
# output ---> print an integer representing discount value for the given total bill amount.

# Logic:
# ------
# 1 ----> read total bill amount from the user.
# 2 ----> extract digits from the total bill amount
# 3 ----> check if digit is in [2,3,5,7]
# 4 ----> the returned value is nothing but result discount.

# list of single digit prime numbers ---> [2,3,5,7]

########################################################################################################
def christmas_offer(num_: int) -> int:
    sum_: int = 0
    while num_ != 0:
        digit: int = num_ % 10
        if digit in (2, 3, 5, 7):
            sum_ = sum_ + digit
        num_ = num_ // 10

    return sum_


if __name__ == '__main__':
    num: int = int(input("Enter the Total Bill amount: "))
    print(christmas_offer(num))
