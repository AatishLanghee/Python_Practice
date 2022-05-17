########################################################################################################
# Question: Find The Sequence Sum

# Given three integers i,j & k,
# a sequence sum is the value of i+(i+1)+(i+1)..+j+(j-1)+(j-1)+..+k
# (increment from i until it equals to j, then decrement j until equals k).
# Given values i,j,k.
# calculate the sequence sum as described.

# int calc_sequence_sum(int,int,int);

# input -------> Three int values
# constraints--> no
# output ------> sum based on given constraints

# i=5
# j=9
# k=6

# ====> 5+6+7+8+9+8+7+6====> 56

# int getSequenceSum(int i,int j,int k) {
#   int sum = 0;
#   int p,q;
#   for(p=i;p!=j;p++)sum += p;
#   for(q=p;q!=k;q--)sum += q;
#   sum += q;
#   return sum;
# }


# Logic:
# ~~~~~
# 1 -----> read i,j & k values from the user.
# 2 -----> s=0
# 3 -----> while i<=j, add i to s, increment i value
# 4 -----> while j!=k, add j to s, decrement j value
# 5 -----> return s
########################################################################################################
def calc_sequence_sum(i: int, j: int, k: int) -> int:
    sum_: int = 0

    while i <= j:
        sum_ = sum_ + i
        i += 1
    j = j - 1
    while j >= k:
        sum_ = sum_ + j
        j -= 1
    return sum_


if __name__ == '__main__':
    x: int = int(input("Enter the number1: "))
    y: int = int(input("Enter the number2: "))
    z: int = int(input("Enter the number2: "))
    print(calc_sequence_sum(x, y, z))
