########################################################################################################
# Question: Sum of even Digits

# Implement a program to calculate sum of even digits present in the given number

# input -------------> a number from the user
# constraint --------> n>0
# output ------------> print sum of even digits

########################################################################################################

def sum_of_even_digits(num_: int) -> None:
    print(f'Given number is: {num_}')
    sum_: int = 0
    if num_ > 0:
        while num_ != 0:
            digit: int = num_ % 10
            if digit % 2 == 0:
                sum_ += digit
            num_ = num_ // 10

    print(f'sum of even digits is: {sum_}')


if __name__ == '__main__':
    num: int = int(input("Enter the number: "))
    sum_of_even_digits(num)
