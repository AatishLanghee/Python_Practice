########################################################################################################
# Question: Digit extraction

# Implement a program to extract digits from the given number

# input -------------> a number from the user
# constraint --------> n>0
# output ------------> print digits in line sep by space

# Logic: Digits extraction

# while(n!=0)
# {
# 	d = n % 10;
# 	print d
# 	n = n / 10;
# }

########################################################################################################
def solution(n: int) -> None:
    while n != 0:
        digit: int = n % 10
        print(digit, end=" ")
        n = n // 10


if __name__ == '__main__':
    num: int = int(input("Enter the number :"))
    solution(num)
