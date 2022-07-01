########################################################################################################
# Question: Sum of Digits

# Implement a program to calculate sum of digits present in the given number

# input -------------> a number from the user
# constraint --------> n>0
# output ------------> print sum of digits

########################################################################################################

def sum_of_digits(num_: int) -> None:
    print(f'Given number is: {num_}')
    sum_: int = 0
    if num_ > 0:
        while num_ != 0:
            digit: int = num_ % 10
            sum_ += digit
            num_ = num_ // 10

        print(f'sum of digits is: {sum_}')


if __name__ == '__main__':
    num: int = int(input("Enter the number: "))
    sum_of_digits(num)
