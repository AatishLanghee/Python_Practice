########################################################################################################
# Question: Integer to English Words

# Convert a non-negative integer num to its English words representation.

# input ------> a number from the user
# con --------> n>0
# output -----> number in English words

# 123 ===> one hundred twenty three
# 9999 ==> Nine Thousand Nine Hundred Ninty Nine

# Logic:
# ~~~~~~
# 1. read an integer value from the user.
# 2. based on positions develop if conditions.

# 2nd approach: Learn recursion
########################################################################################################
def first_approach(num_: str, ) -> str:
    num_len: int = len(num_)
    unit_place: list = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens_place: list = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninty"]
    tens_place_more: list = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                             "Nineteen"]
    if num_len == 1:
        return unit_place[int(num_)]
    elif num_len == 2:
        if num_[1] == "0":
            return tens_place[int(num_[0]) - 1]
        elif num_[0] == "1":
            return tens_place_more[int(num_[1]) - 1]
        elif num_[0] != "1":
            return tens_place[int(num_[0]) - 1] + " " + unit_place[int(num_[1])]
    elif num_len == 3:
        if num_[1] == "0" and num_[2] == "0":
            return unit_place[int(num_[0])] + " Hundred "
        elif num_[1] == "1":
            return unit_place[int(num_[0])] + " Hundred" + " " + tens_place_more[int(num_[2]) - 1]
        elif num_[1] == "0":
            return unit_place[int(num_[0])] + " Hundred" + " " + unit_place[int(num_[2])]
        elif num_[2] == "0":
            return unit_place[int(num_[0])] + " Hundred" + " " + tens_place[int(num_[1]) - 1]
        else:
            return unit_place[int(num_[0])] + " Hundred" + " " + tens_place[int(num_[1]) - 1] + " " + \
                   unit_place[int(num_[2])]
    elif num_len == 4:
        if num_[1] == "0" and num_[2] == "0" and num_[3] == "0":
            return unit_place[int(num_[0])] + " Thousand "
        elif num_[2] == "0" and num_[3] == "0":
            return unit_place[int(num_[0])] + " Thousand " + unit_place[int(num_[1])] + " Hundred "
        elif num_[1] == "0" and num_[3] == "0":
            return unit_place[int(num_[0])] + " Thousand " + tens_place[int(num_[2]) - 1]
        elif num_[1] == "0" and num_[2] == "0":
            return unit_place[int(num_[0])] + " Thousand " + unit_place[int(num_[3])]
        elif num_[1] == "0" and num_[2] == "1":
            return unit_place[int(num_[0])] + " Thousand " + tens_place_more[int(num_[3]) - 1]
        elif num_[3] == "0":
            return unit_place[int(num_[0])] + " Thousand " + unit_place[int(num_[1])] + " Hundred" + " " + \
                   tens_place[int(num_[2]) - 1]
        elif num_[2] == "0":
            return unit_place[int(num_[0])] + " Thousand " + unit_place[int(num_[1])] + " Hundred" + " " + \
                   unit_place[int(num_[3])]
        elif num_[2] == "1":
            return unit_place[int(num_[0])] + " Thousand " + unit_place[int(num_[1])] + " Hundred" + " " + \
                   tens_place_more[int(num_[3]) - 1]
        elif num_[1] == "0":
            return unit_place[int(num_[0])] + " Thousand " + tens_place[int(num_[2]) - 1] + " " + \
                   unit_place[int(num_[3])]
        else:
            return unit_place[int(num_[0])] + " Thousand " + unit_place[int(num_[1])] + " Hundred" + " " + \
                   tens_place[int(num_[2]) - 1] + " " + unit_place[int(num_[3])]


def second_approach(num_: int,) -> str:
    below_ten: list = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    below_twenty: list = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                          "Eighteen", "Nineteen"]
    below_hundred: list = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninty"]

    if num_ < 10:
        return below_ten[num_] + " "
    elif num_ < 20:
        return below_twenty[num_ - 10] + " "
    elif num_ < 100:
        return below_hundred[(num_ // 10) - 1] + " " + second_approach((num_ % 10),) + " "
    elif num_ < 1000:
        return second_approach((num_ // 100),) + "Hundred " + \
                second_approach((num_ % 100),)
    elif num_ < 10000:
        return second_approach((num_ // 1000),) + "Thousand " + \
               second_approach((num_ % 1000), )


if __name__ == "__main__":
    number: str = input("Enter the Number :")
    print(first_approach(number, ))

    if number == "0":
        print("Zero")
    else:
        print(second_approach(int(number),))
