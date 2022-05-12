########################################################################################################
# Question: Decimal to Binary

# A network protocol specifies how data is exchanged via transmission media.
# The protocol converts each message into a stream of 1's and 0's.
# Given a decimal number, write an algorithm to convert the number into a binary form.

# input ---------> a number
# constraint ----> n>=0
# output --------> binary number

# Logic:
# ------
# decimal:
# extract digits ----> %10
# reverse -----------> *10
# next n value ------> /10
#
# binary:
# digit ----> %2
# next -----> /2
#
# 1. read a number from the user
# 2. calculate n%2 and store in an array
# 3. repeat this by eval n/2 until n>0 or n!=0
# 4. our data is in array
# 5. print the array in reverse
########################################################################################################

def reverse_array(temp_list: list) -> str:
    return "".join(str(x) for x in temp_list[::-1])


def decimal_to_binary(num_: int) -> None:
    print(f'Given number is: {num_}')
    output_array: list = []
    if num_ >= 0:
        while num_ != 0:
            digit: int = num_ % 2
            output_array.append(digit)
            num_ = num_ // 2

        print(reverse_array(output_array))


if __name__ == '__main__':
    num: int = int(input("Enter the number: "))
    decimal_to_binary(num)
