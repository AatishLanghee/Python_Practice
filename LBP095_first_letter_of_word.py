########################################################################################################
# Question: Print First Letter of each Word

# Implement a function/Method to return first character in each word from the given input string.

# input-----> a string
# con-------> no
# output ---> first character in each string

# ip = welcome to python programming
# op = wtpp
########################################################################################################
def first_approach(str_: str) -> str:
    word: str
    op_str: list = []
    for word in str_.lower().split(" "):
        op_str.append(word[0])

    return "".join(op_str)


if __name__ == "__main__":
    string: str = input("Enter a string :")
    print(first_approach(string,))
