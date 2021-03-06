########################################################################################################
# Question: Reverse Integer

# Given an integer x, return x with its digits reversed.

# input---------> a number from user
# constraint ---> n>=0
# output -------> reverse of the given number

# Logic:
# ------
# while(n!=0)
# {
# 	d=n%10;	//extracting digit
# 	r=r*10+d;//logic reverse
# 	n=n/10;	//change or update value of n
#
# }
########################################################################################################
def reverse_number(num_: int) -> None:
    print(f'Given number is: {num}')
    reverse_num: int = 0
    if num_ > 0:
        while num_ != 0:
            digit: int = num_ % 10
            reverse_num = reverse_num * 10 + digit
            num_ = num_ // 10
        print(f'Reverse of given number is: {reverse_num}')


if __name__ == '__main__':
    num: int = int(input("Enter the number: "))
    reverse_number(num)
