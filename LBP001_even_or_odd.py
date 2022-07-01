########################################################################################################
# Question: Even or odd number

# Program to check whether the given number is even or odd number.

# inputs ----------> a number from the user
# output  ---------> even or odd or invalid
# constraint ------> n>=0

# Logic: if number is divisible by 2 then it is even number else odd number.
########################################################################################################
def solution(n: int) -> str:
    if n % 2 == 1:
        return "Odd"
    return "Even"


if __name__ == '__main__':
    num: int = int(input("Enter the number :"))
    print(solution(num))
