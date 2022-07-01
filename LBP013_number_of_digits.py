########################################################################################################
# Question: Number of digits

# Implement a program to calculate number of digits in the given number

# input -------------> a number from the user
# constraint --------> n>0
# output ------------> print number of digits in the number

# Logic:
# ------
# count=0
# while(n!=0)
# {
#     d=n%10;
#     count++
#     n=n/10
# }
########################################################################################################

def number_of_digits(num_: int) -> None:
    print(f'Given number is: {num}')
    count: int = 0
    if num_ > 0:
        while num_ != 0:
            digit: int = num_ % 10
            count += 1
            num_ = num_ // 10
        print(f'Number of digits in the given number is: {count}')


if __name__ == '__main__':
    num: int = int(input("Enter the number: "))
    number_of_digits(num)
