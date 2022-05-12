########################################################################################################
# Question: Program to check whether the given number is palindrome or not.

# A number is said to palindrome if that remains the same when its digits are reversed.

# input -----> a number from the user
# constraint-> n>0
# output ----> Yes or No

# Logic:
# ------
# 1. read a number from the user.
# 2. calculate reverse value
# 	r=0
# 	while(n!=0)
# 	{
# 		d=n%10;
# 		r=r*10+d;
# 		n=n/10;
# 	}
# 3. we have to compare original number and reversed number.
# 4. if both are same print Yes or No

########################################################################################################

def palindrome(num_: int) -> None:
    print(f'Given number is: {num_}')
    original_num: int = num_
    reverse_num: int = 0
    if num_ > 0:
        while num_ != 0:
            digit: int = num_ % 10
            reverse_num = reverse_num * 10 + digit
            num_ = num_ // 10

    if reverse_num == original_num:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    num: int = int(input("Enter the number: "))
    palindrome(num)
