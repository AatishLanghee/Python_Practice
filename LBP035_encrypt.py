########################################################################################################
# Question: encryption

# The IT company "Soft ComInfo" has decided to transfer its messages through the N/W using new encryption technique.
# The company has decided to encrypt the data using the non-prime number concept. The message is in the form of a number
# and the sum of non-prime digits present in the message is used as the encryption key.
# Write an algorithm to determine the encryption key.

# input ------> The input consists of an integer numMsg representing the numeric form of the message.
# output ------> print an integer representing the encryption key.

# note: Digit 1 and 0 are considered as a prime number.

# prime digits -----> 0,1,2,3,5,7
# non-prime --------> 4,6,8,9

# Logic:
# ~~~~~~
# 1-------> read a number numMsg from the user
# 2-------> find non-prime digits
# 3 ------> all these non prime digits store it in key
# 4 ------> print the value of key
########################################################################################################
def encrypt(num: int) -> int:
    sum_: int = 0
    digit: str
    for digit in str(num):
        if int(digit) in (4, 6, 8, 9):
            sum_ = sum_ + int(digit)
    return sum_


if __name__ == "__main__":
    num_msg: int = int(input("Enter the number message :"))
    print(encrypt(num_msg))
