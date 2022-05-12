########################################################################################################
# Question: Niven Number

# Write a program to accept a number and check and display whether it is a Niven Number or not.
# Niven Number is that a number which is divisible by its sum of digits.

# input -----> a number
# constraint-> n>0
# output ----> Niven Number or Not

# Logic:
# ------
# 1. read a number from user
# 2. cal sum of its digits.
# 3. divide the original number with sum of its digits
# 4. if it is divisible then print Niven Number else Not.

########################################################################################################
def check_niven(num_: int) -> str:
    original_num: int = num_
    sum_of_digit: int = 0
    if num_ > 0:
        while num_ != 0:
            digit: int = num_ % 10
            sum_of_digit = sum_of_digit + digit
            num_ = num_ // 10

        if original_num % sum_of_digit == 0:
            return "Niven Number"
        else:
            return "Not niven number"


if __name__ == '__main__':
    num: int = int(input("Enter the number: "))
    print(check_niven(num))
