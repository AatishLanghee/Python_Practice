########################################################################################################
# Question: War of Numbers

# There is a great war between the even and odd numbers. Many numbers already lost their lives in this war, and
# it's your task to end this. You have to determine which group sums larger, the even or the odd, the larger group wins.
# Create a function that takes an array of integers, sums the even and odd numbers separately,
# then return the difference between sum of even and odd numbers.

# Note: if result is -ve convert it into +ve.

# input --------> number and array elements
# constraint ---> no
# output -------> difference between sum of even and odd numbers

# Logic:
# ~~~~~~~
# 1 ------------> read array size
# 2 ------------> read the elements
# 3 ------------> sum of even elements and sum of odd elements
# 4 ------------> diff = sum of even - sum of odd elements
# 5 ------------> if diff>0 then print diff else -diff
########################################################################################################
def calculate_diff(array: list) -> int:
    even_sum: int = 0
    odd_sum: int = 0
    data_: int
    for data_ in array:
        if data_ % 2 == 0:
            even_sum = even_sum + data_
        else:
            odd_sum = odd_sum + data_

    diff: int = even_sum - odd_sum
    if diff < 0:
        return diff * -1
    else:
        return diff


if __name__ == "__main__":
    len_array: int = int(input("Enter the len of array :"))
    array_lst: list = []
    i: int = 1
    while i <= len_array:
        data: int = int(input(f"Enter the {i} element of array :"))
        array_lst.append(data)
        i = i + 1
    print(calculate_diff(array_lst))
