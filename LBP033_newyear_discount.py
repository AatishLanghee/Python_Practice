########################################################################################################
# Question: e-commerce company newyear discount

# An e-commerce company plans to give their customers a discount for the newyear holiday. The discount will be
# calculated on the basis of the bill amount of the order placed. The discount amount is the sum of all the odd digits
# in the customers total bill amount. if no odd digits is present in the bill amount, then discount will be zero.

# input-> the input consists of an integer bill amount, representing the customers total bill amount.
# output --> print an integer representing the discount for the given total bill amount.
# constraint ---> n>0

# Logic:
# ~~~~~~
# 1 ----------> read bill amount
# 2 ----------> extract digits from bill amount
# 3 ----------> sum of all odd digits
# 4 ----------> sum is nothing but discount
########################################################################################################
def newyear_discount(bill_: int) -> int:
    discount: int = 0

    while bill_ != 0:
        digit: int = bill_ % 10
        if digit % 2 == 1:
            discount = discount + digit
        bill_ = bill_ // 10

    return discount


if __name__ == "__main__":
    bill: int = int(input("Enter the bill amount :"))
    print(f"Newyear discount is:{newyear_discount(bill)}")
