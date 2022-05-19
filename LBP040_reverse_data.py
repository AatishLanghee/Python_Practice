########################################################################################################
# Question: reverse the data first

# A company wishes to transmit data to another server. The data consists of numbers only. To secure the data during
# transmission, they plan to reverse the data during transmission, they plan to reverse the data first.
# Write an algorithm to reverse the data first

# input -----> an integer data, representing the data to be transmitted
# output ----> print an integer representing the given data in reverse form

# Logic:
# ~~~~~~
# 1--------------> read an integer
# 2 -------------> extract digits
# 3 -------------> construct a number based on digits and math formula
# 4 -------------> return reverse
########################################################################################################
def reverse_data(d: int) -> int:
    output_data: int = 0
    while d != 0:
        digit: int = d % 10
        output_data = output_data * 10 + digit
        d = d // 10
    return output_data


def second_approach(d: int) -> int:
    return int(str(d)[::-1])


if __name__ == "__main__":
    data: int = int(input("Enter the data :"))
    print(reverse_data(data))
    print(second_approach(data))
