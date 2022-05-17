########################################################################################################
# Question: A Special two-digit number

# A special two-digit number is a number such that when the sum of its digits is added to the product of its digits,
# the result should be equal to the original two-digit number.

# Implement a program to accept a two-digit number and check whether it is a special two-digit number or not.

# input -----> a two digit number
# constraint-> 10<=n<=99
# output ----> special two digit number or not

# Logic:
# ------
# 1. extract digits from the given number.
# 2. cal new number = sum of those digits + product of those digits.
# 3. compare new number with old number.
# 4. if equal print "A special two-digit number" else "not"
########################################################################################################
def special_number(num_: int) -> str:
    original_num: int = num_
    sum_: int = 0
    product_: int = 1
    if 10 <= num_ <= 99:
        while num_ != 0:
            digit_: int = num_ % 10
            sum_ = sum_ + digit_
            product_ = product_ * digit_
            num_ = num_ // 10

        if (sum_ + product_) == original_num:
            return "Special two digit number"
        else:
            return "Not a special two digit number"


if __name__ == '__main__':
    num: int = int(input("Enter the number: "))
    print(special_number(num))
