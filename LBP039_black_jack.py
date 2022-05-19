########################################################################################################
# Question: BlackJack

# Implement the following function
# 	int black_jack(int n1,int n2);

# the function accepts two +ve integers n1 and n2 as its arguments.
# Implement the function on given two values to return an int value as follows:
# return whichever value is nearest to 21 without going over. Return if they go both go over ( greater than 21 ).

# input --------> two int values n1 and n2
# constraint ---> no
# output -------> 0 or n1 or n2

# Logic:
# ~~~~~~
# 1 ----------------> read two numbers
# 2 ----------------> if both are >21 then return 0
# 3 ----------------> if n1>21, then return n2
# 4 ----------------> if n2>21, then return n1
# 5 ----------------> max of n1 & n2
########################################################################################################
def black_jack(num1: int, num2: int) -> int:
    max_value: int = 21

    if num1 > max_value and num2 > max_value:
        return 0
    elif num1 > max_value:
        return num2
    elif num2 > max_value:
        return num1
    else:
        return max(num1, num2)


if __name__ == "__main__":
    n1: int = int(input("Enter the first number :"))
    n2: int = int(input("Enter the second number :"))
    print(black_jack(n1, n2))
