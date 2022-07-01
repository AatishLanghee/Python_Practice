########################################################################################################
# Question: Duck Number

# Program to read a number and check whether it is duck number or not.

# A duck number is a number which has zeros present in it, but no zero present in the begining of the number.

# input-------> a number from the user
# constraint --> n>=0
# output------> Yes or No

# Logic:
# ------
# 1. extract digits one by one
# 2. and check whether d==0 or not
# 3. if d==0 then res=Yes and terminate
# 4. res=False
# 5. print res
########################################################################################################
def duck_number(num_: str) -> None:
    print(f'Given number is: {num_}')
    temp_num: int = int(num_)
    if temp_num >= 0:
        if num_[0] == "0":
            print("Not a duck number.")
        else:
            if "0" in str(temp_num):
                print("Duck number.")
            else:
                print("Not a duck number.")


if __name__ == '__main__':
    num: str = input("Enter the number: ")
    duck_number(num)
