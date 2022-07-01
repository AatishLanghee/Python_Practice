########################################################################################################
# Question: Coffee Cups

# For each of the 6 coffee cups I buy, I get a 7th cup free. In total, I get 7 cups.
# Implement a program that takes n cups bought and print as an integer the total number of cups I would get.

# input -------------> n number of cups from user
# constraints -------> n>0
# output ------------> number of cups present have


# 2 --------> 2
# 6 --------> 7
# 12 -------> 14 etc

# Logic: number of cups bought + free cups [n/6] ===> n+(n/6)

########################################################################################################
def solution(n: int) -> int:
    return n + (n // 6)


if __name__ == '__main__':
    num: int = int(input("Enter the number :"))
    print(solution(num))
