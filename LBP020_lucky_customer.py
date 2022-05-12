########################################################################################################
# Question: Lucky Customer

# An e-commerce website wishes to find the lucky customer who will be eligible for full value cash back. For this
# purpose,a number N is fed to the system. It will return another number that is calculated by an algorithm. In the
# algorithm, a sequence is generated, in which each number n is the sum of the two preceding numbers. Initially the
# sequence will have two 1's in it. 1,1,2,3,5,8.. and so on. The System will return the Nth number from the generated
# sequence which is treated as the order ID. The lucky customer will be one who has placed that order. Write an
# algorithm to help the website find the lucky customer.

# input --------> a number
# constraint ---> n>0
# output -------> a number

# Logic:
# ------
# fibonacci series
# 0,1,1,2,3,5,8...


# 0====>0
# 1====>1
# 2====>0+1=1
# 3====>1+1=2
# 4====>1+2=3
# 5====>2+3=5
# 6====>3+5=8
# 7====>5+8=13
# 8====>8+13=21
########################################################################################################
def lucky_customer(num_: int) -> int:
    if num_ >= 0:
        if num_ == 0 or num_ == 1:
            return num_
        else:
            return lucky_customer(num_ - 1) + lucky_customer(num_ - 2)


if __name__ == '__main__':
    num: int = int(input("Enter the number: "))
    print(lucky_customer(num))
