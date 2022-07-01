########################################################################################################
# Question: Sum of Digits  divisible by 3

# Implement a program to calculate sum of digits that are divisible by 3 in the given number

# input -------------> a number from the user
# constraint --------> n>0
# output ------------> print sum of digits that are divisible by 3

# Logic1:
# -------
# s=0
# while(n!=0)
# {
#     d=n%10;
#     if d%3==0
#        s=s+d
#     n=n/10
# }
########################################################################################################

def sum_of_digits_divisible_by_3(num_: int) -> None:
    print(f'Given number is: {num}')
    sum_: int = 0
    if num_ > 0:
        while num_ != 0:
            digit: int = num_ % 10
            if digit % 3 == 0:
                sum_ += digit
            num_ = num_ // 10
        print(f'sum of digits divisible by 3 is: {sum_}')


if __name__ == '__main__':
    num: int = int(input("Enter the number: "))
    sum_of_digits_divisible_by_3(num)
