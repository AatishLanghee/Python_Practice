########################################################################################################
# Question: Say "Hello" Say "Bye"

# Write a function that takes a string name and number num (either 1 or 0) and
# return "Hello"+name if number is 1,
# otherwise "Bye"+name.

# input ------> a string from the user
# constraint -> no
# output -----> a string

# prakash,1 -----> Hello prakash
# java,0 --------> Bye java
# python,1 ------> Hello python

# Logic:
# ~~~~~~
# 1. read a string from the user as s
# 2. read a number from the user as num
# 3. if num is 1 then print "Hello" + s
# 4. if num is 0 then print "Bye" s
########################################################################################################
def first_approach(str_: str, num_: int) -> str:
    if num_ == 1:
        return "Hello " + str_
    return "Bye " + str_


if __name__ == "__main__":
    string: str = input("Enter the Name :")
    num__: int = int(input("Enter the number :"))
    print(first_approach(string, num__))
