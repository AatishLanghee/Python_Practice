########################################################################################################
# Question: chess board

# You are given coordinates, a string that represents the coordinates of a square of the chess board.
# Below is the chess board for your reference.

# Return True if the square is in white, and false if the square is in Black.

# The coordinates will always represent a valid chess board square.
# The coordinates will always have the letter first, and the number second.

# input ----------> a string
# constraint -----> length of the string is 2, a<=c[0]<=h and 1<=c[1]<=8
# output ---------> true or false
########################################################################################################
def solution(string_: str) -> str:
    if ((ord(string_[0]) - ord('a')) + 1) % 2 != int(string_[1]) % 2:
        return "true"
    else:
        return "false"


if __name__ == "__main__":
    string: str = input("Enter the string :")
    print(solution(string))
