########################################################################################################
# Question: weird or not weird

# Given an integer n, perform the following conditional actions,
# if n is odd, print weird,
# if n is even and in the inclusive range of 2 to 5, print Not Weird.
# if n is even and in the inclusive range of 6 to 20, print Weird.
# if n is even and greater than 20, print Not Weird.

# input-----> a number from the user
# constraint-> 1<=n<=100
# output----> Weird or Not Weird

# Logic:

# if (n%2!=0)
# {
# 	print "Weird"
# }
# else
# {
# 	if n>=2 and n<=5 then print "Not Weird"
# 	else if n>=6 and n<=20 print "Weird"
# 	else print "Not Weird"
# }

########################################################################################################
def solution(n: int) -> str:
    if n % 2 == 1:
        return "Weird"

    if n in range(2, 6):
        return "Not Weird"
    elif n in range(6, 21):
        return "Weird"

    return "Not Weird"


if __name__ == '__main__':
    num: int = int(input("Enter the number :"))
    print(solution(num))
