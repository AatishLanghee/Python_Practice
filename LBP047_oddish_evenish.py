########################################################################################################
# Question: Oddish or Evenish

# Create a function that determines whether a number is Oddish or Evenish. A number is Oddish if the sum of all of
# its digits is Odd, and number is Evenish if the sum of all of its digits is even, if a number
# is Oddish return Oddish else return Evenish.

# input ----------> a number
# constraint -----> n>0
# output ---------> Oddish or Evenish

# Logic:
# ~~~~~~
# 1 ---------> read a number
# 2 ---------> cal sum of its digits
# 3 ---------> if sum is even then print Evenish
# 4 ---------> else print Oddish
########################################################################################################
def oddish_evenish(num_: int) -> str:
    sum_: int = 0

    while num_ != 0:
        digit: int = num_ % 10
        sum_ = sum_ + digit
        num_ = num_ // 10

    if sum_ % 2 == 0:
        return "Evenish"
    else:
        return "Oddish"


if __name__ == "__main__":
    num: int = int(input("Enter the number :"))
    print(oddish_evenish(num))
