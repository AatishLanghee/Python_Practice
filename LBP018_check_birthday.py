########################################################################################################
# Question: Check BirthDay

# Lisa always forgets her birthday which is on 5th July.
# So develop a function/method which will be helpful to remember her birthday.

# The function/method check_birthday return an integer 1, if it is her birthday else return 0.
# the function/method check_birthday accepts two arguments.
# Month, a string representing the month of her birth and
# day, an integer representing the date of her birthday.

# input -----------> month & day
# constraints -----> no
# output ----------> 1 or 0

# Logic:
# ------
# 1. read month and day from the user.
# 2. user given month value we have to compare with july ---> Cond1
# 3. user given date value we have to compare with 5--------> Cond2
# 4. if cond1 and cond2 both are satisfied then return 1 else 0.
########################################################################################################
def check_birthday(month_: str, day_: int) -> None:
    if month_.lower() == "july" and day_ == 5:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    month: str = input("Enter the month: ")
    day: int = int(input("Enter the day: "))
    check_birthday(month, day)
