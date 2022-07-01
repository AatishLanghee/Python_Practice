########################################################################################################
# Question: Bookshelf

# The e-commerce company Bookshelf wishes to analyse its monthly sales data between minimum range 30 to max range 100.
# The company has categorized these book sales into four groups depending on the number of sales with the help of
# these groups the company will know which stock they should increase or decrease in their inventory
# for the next month. the groups are as follows

# sales range		groups
# 30-50 ------------------> D
# 51-60 ------------------> C
# 61-80 ------------------> B
# 81-100 -----------------> A

# write an alg to find the group for the given book sale count.

# input--------> an integer salesCount represent total sales of a book
# output-------> a character representing the group of given sale count
# constraint---> 30<=saleCount<=100

########################################################################################################
def solution(n: int) -> str:
    if 30 <= n <= 100:
        if 30 <= n <= 50:
            return "D"
        elif 51 <= n <= 60:
            return "C"
        elif 61 <= n <= 80:
            return "B"
        else:
            return "A"


if __name__ == '__main__':
    num: int = int(input("Enter the number :"))
    print(solution(num))
