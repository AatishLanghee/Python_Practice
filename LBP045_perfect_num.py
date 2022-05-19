########################################################################################################
# Question: Perfect Number

# Create a function that tests whether an integer is a perfect number.
# A perfect number is a number that can be written as sum of its factors.
# (equal to sum of its proper divisors) excluding the number itself.

# Eg:
# 6 =======> 1,2,3,6 ====> 1+2+3=6
# 8 =======> 1,2,4,8 ====> 1+2+4=7

# Logic:
# ~~~~~
# 1. read a number from the user.
# 2. divide the number with numbers from 1 to n-1
# 3. if it is divisible (factor) add to sum variable.
# 4. check sum and original number are same or not
# 5. same print "perfect number" else "not"
# 7. true or false
########################################################################################################
def perfect_num(n: int) -> bool:
    sum_: int = 0
    for i in range(1, n):
        if n % i == 0:
            sum_ = sum_ + i

    if sum_ == n:
        return True
    else:
        return False


if __name__ == "__main__":
    num: int = int(input("Enter the number :"))
    print(perfect_num(num))
