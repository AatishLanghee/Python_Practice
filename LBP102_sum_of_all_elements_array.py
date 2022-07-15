########################################################################################################
# Question: Student Rewarded Question

# You are given a string representing an attendance record for a student.
# The record only contains the following three characters:
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.

# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent)
# or more than two continuous 'L' (late).

# You need to return whether the student could be rewarded according to his attendance record.

# input ------> a string from the user
# con --------> non empty string
# output -----> Yes or No

# PPP ---> Yes
# PAP ---> Yes
# PAA ---> No
# APA ---> No
# PPL ---> Yes
# PLL ---> Yes
# LLL ---> No
# LPAPLPPLL --> Yes

# Logic:
# ~~~~~~
# 1. read a string from the user.
# 2. count number of A's ---> C1
# 3. count continues three L's  ---> C2
# 4. if c1 or c2 is true then print No
# 5. else "Yes"
########################################################################################################
def first_approach(str_: str) -> str:
    char: str
    a_count: int = 0
    for i, char in enumerate(str_):
        if char == "A":
            a_count += 1
            if a_count > 1:
                return "No"
        elif char == "L":
            if (i < len(str_) - 2) and str_[i+1] == "L" and str_[i+2] == "L":
                return "No"
    return "Yes"


if __name__ == "__main__":
    string: str = input("Enter a string :")
    print(first_approach(string,))
