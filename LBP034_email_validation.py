########################################################################################################
# Question: Email validation

# Email name should be starts with alphabet and should be followed by number or underscore. It should contain either
# numbers or underscore finally ends with gmail.com only. Then given email id is true otherwise false.

# input ------> email id
# constraint -> lowercase alphabet [a-z] followed by underscore or digit and gmail.com
# output -----> true or false

# abc@gmail.com --------> false
# abc1@gmail.com -------> true
# abc_@gmail.com -------> true
# abc1_@gmail.com ------> false
# abc__@gmail.com ------> false
# abc34@gmail.com ------> false
# abc8@gmail.com -------> true
# abc@facebook.com -----> false
#
# Logic:
# ~~~~~~
# 1. read a string
# 2. first compare all alphabets are there or not.
# 3. after alphabets number or _
# 4. ends with @gmail.com
# 5. 2,3 and 4 ---> true else false
########################################################################################################
def first_approach(email_: str) -> bool:
    i: int = 0
    if not email_[i].isalpha():
        return False

    while email_[i].isalpha():
        i = i + 1

    if email_[i].isdigit() or email_[i] == "_":
        i = i + 1
        if email_[i::] == "@gmail.com":
            return True
        else:
            return False
    else:
        return False


def second_approach(email_: str) -> bool:
    import re
    output: bool = re.fullmatch("[a-z]+[0-9|_]@gmail[.]com", email_)
    if output is None:
        return False
    else:
        return True


if __name__ == "__main__":
    email: str = input("Enter the email address :")
    print(first_approach(email))
    print(second_approach(email))
