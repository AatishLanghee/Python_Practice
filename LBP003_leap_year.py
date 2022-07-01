########################################################################################################
# Question: Leap Year

# input------> year from the user
# constraint-> no constraint
# output-----> leap year or not leap year

# hint: for century year if it is divisible by 400 then only it is leap year

# Logic:
# ~~~~~~~~~~
# if (year%4==0 and year%100!=0) or year%400==0
#     True
# else
#     False
########################################################################################################
def solution(year_: int) -> str:
    if (year_ % 4 == 0 and year_ % 100 != 0) or year_ % 400 == 0:
        return "Leap Year"
    return "Not a leap year"


if __name__ == '__main__':
    num: int = int(input("Enter the year :"))
    print(solution(num))
