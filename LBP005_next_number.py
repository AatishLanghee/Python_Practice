########################################################################################################
# Question: Next Number

# implement a program that takes a number as an argument, increments the number by +1 and returns the result
#
# input ----------> a number from the user
# constraints-----> no constraints
# output ---------> an incremented value

########################################################################################################
def solution(n: int) -> int:
    return n + 1


if __name__ == '__main__':
    num: int = int(input("Enter the number :"))
    print(solution(num))
