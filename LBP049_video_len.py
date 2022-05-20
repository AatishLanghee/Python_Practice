########################################################################################################
# Question: video length in seconds

# Accept video length in minutes the format is mm:ss in String format, create a function that takes video length
# and return it in seconds.

# input --------> video length in mm:ss
# constraint----> no
# output -------> length in seconds

# 01:00 ====> 60
# 02:02 ====> 122
# 02:01 ====> 121
#
# Logic:
# ~~~~~
# 1-----------> read mm:ss value in the form of String.
# 2 ----------> extract mm value and convert into int--->m.
# 3 ----------> extract ss value and convert into int--->s.
# 4 ----------> print m*60+s
########################################################################################################
from typing import List


def cal_sec(vid_len: str) -> int:
    min_, sec = vid_len.split(":")
    return int(sec) + int(min_) * 60


def second_approach(vid_len: str) -> int:
    l: List[str] = vid_len.split(":")
    # L=['02','00']
    if l[0][0] == '0':
        n1 = int(l[0][1])
    else:
        n1 = int(l[0][0]) * 10 + int(l[0][1])
    if l[1][0] == '0':
        n2 = int(l[1][1])
    else:
        n2 = int(l[1][0]) * 10 + int(l[1][1])
    return n1 * 60 + n2


if __name__ == "__main__":
    video_len: str = input("Enter the video in mm:ss format :")
    print(cal_sec(video_len))
    print(second_approach(video_len))
