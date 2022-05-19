########################################################################################################
# Question: New year holiday discount

# An e-Commerce company plans to give their customers a discount for the newyear holiday.
# The discount will be calculated on the basis of the bill amount of the order place.
# The discount amount is the product of the sum of all odd digits and the sum of all even digits of
# the customers total bill amount.

# input ----> an integer bill amount, representing the total bill amount of the customer.
# output ---> print an integer representing the discount amount for the given total bill.

# Logic:
# ~~~~~~
# 1. read bill amount as an integer.
# 2. sum of even digits and sum of odd digits in the given number.
# 3. se and so, discount = se*so
# 4. print discount
########################################################################################################
def discount(num: int) -> int:
    even_sum_: int = 0
    odd_sum_: int = 0

    while num != 0:
        digit: int = num % 10
        if digit in (1, 3, 5, 7, 9):
            odd_sum_ = odd_sum_ + digit
        else:
            even_sum_ = even_sum_ + digit

        num = num // 10

    return odd_sum_ * even_sum_


if __name__ == "__main__":
    bill: int = int(input("Enter the bill amount :"))
    print(discount(bill))
