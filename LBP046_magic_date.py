########################################################################################################
# Question: Magic Date

# Program to read date, month and year from the user and check whether it is magic date or not.
# Here are the rules for magic date.

# dd-mm-yyyy
# dd/mm/yyyy
# dd mm yyyy ----> C lang

# 1) mm*dd is a 1-digit number that matches the last digit in YYYY
# 2) mm*dd is a 2-digit number that matches the last two digits in YYYY
# 3) mm*dd is a 3-digit number that matches the last three digits in YYYY
#
# 1-1-2001 ===> 1*1=1
# 1-1-2002 ===> 1*1=1
# 5-2-2010 ===> 5*2=10

# Logic:
# ~~~~~~
# 1 -------> read dd,mm and yyyy
# 2 -------> multiply dd*mm
# 3 -------> if the result is ending at yyyy ----> magic date
# 4 -------> else not magic date
########################################################################################################
def magic_date(d: int, m: int, y: int) -> bool:
    prod: int = d * m
    if prod < 10 and prod == y % 10:
        return True
    elif prod < 100 and prod == y % 100:
        return True
    elif prod < 1000 and prod == y % 1000:
        return True
    else:
        return False


if __name__ == "__main__":
    date: int = int(input("Enter the date value in dd:"))
    month: int = int(input("Enter the month value in mm:"))
    year: int = int(input("Enter the year value in yyyy:"))
    print(magic_date(date, month, year))
