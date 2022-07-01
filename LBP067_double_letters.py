########################################################################################################
# Question: Double Letters

# Create a function that takes a word and returns true if the word has two consecutive identical letters.

# input ---------> A string
# constraint-----> No
# output --------> true or false

# abbc -----> true
# abcd -----> false
# abab -----> false

# Logic:
# ~~~~~
# 1. read a string from the user
# 2. declare found as false
# 3. if ith element and i+1th element are same, then assign found=true
# 4. else found =false
# 5. print found value
########################################################################################################
def first_approach(str_: str) -> bool:
    for item in range(len(str_)):
        if (item < len(str_) - 1) and str_[item] == str_[item + 1]:
            return True
    return False


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(first_approach(string))
