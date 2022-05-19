########################################################################################################
# Question: Create PIN using Three given numbers

# "Secure Assets Private Ltd", a small company that deals with lockers has recently started manufacturing digital
# locks which can be locked and unlocked using PINs (passwords). You have been asked to work on the module that is
# expected to generate PINs using three input numbers.

# The three given input numbers will always consist of three digits each
# i.e. each of them will be in the range >=100 and <=999.

# Below are the rules for generating the PIN.

# 1. The PIN should be made up of 4 digits.
# 2. The unit (ones) position of the PIN should be the least of the units position of the three numbers.
# 3. The tens position of the PIN should be the least of the tens position of the three input numbers.
# 4. The hundreds position of the PIN should be least of the hundreds position of the three numbers.
# 5. The thousands position of the PIN should be the max of all digits in the three input numbers.

# input ----------> three numbers
# constraints ----> all the numbers must be in the range of >=100 and <=999
# output ---------> PIN value
########################################################################################################
def max_digit(num: int) -> int:
    max_num: int = 0

    while num != 0:
        digit: int = num % 10
        if digit > max_num:
            max_num = digit
        num = num // 10

    return max_num


def generate_pin(n1: int, n2: int, n3: int) -> int:
    digit_4: int = min(n1 % 10, n2 % 10, n3 % 10)
    digit_3: int = min((n1 % 100)//10, (n2 % 100)//10, (n3 % 100)//10)
    digit_2: int = min(n1 // 100, n2 // 100, n3 // 100)
    digit_1: int = max(max_digit(n1), max_digit(n2), max_digit(n3))

    return digit_1 * 1000 + digit_2 * 100 + digit_3 * 10 + digit_4


if __name__ == '__main__':
    number1: int = int(input("Enter the first number: "))
    number2: int = int(input("Enter the second number: "))
    number3: int = int(input("Enter the third number: "))
    print(f"Generated PIN: {generate_pin(number1, number2, number3)}")
