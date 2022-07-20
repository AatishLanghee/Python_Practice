########################################################################################################
# Question: binary search

# Implement a program to search for an element in an array.

# input -------> size, array elements and element to search
# con ---------> size<100
# output ------> search for the given element

# Linear search Time complexity:
# key=1 =====> 1=1 -----------------> Best
# key=3 =====> 1+1+1=3 -------------> Avg
# key=5 =====> 1+1+1+1+1=5 ---------> Worst

# List|Array must be in order
#
# 5,6,7,8,9
# 0 1 2 3 4

# low=0
# high=4

# while(low!=high){
# 	mid = (low+high)/2; ----> m=2
# 	if(key==mid)
# 	return mid;
# 	else if(key>a[mid])
# 	low=mid+1
# 	else
# 	high=mid-1
# }

# key=7 ----> 0!=4 ---> m=2 ---> key==a[mid] ----> 7==a[2] --->7==7 ---> Success
# key=5 ----> 0!=4 ---> m=2 ---> key==a[mid] ----> 5==a[2] --->5==7
# 					   ----> 5>a[2] ---->5>7 x
# 					   ----> ------ ---->
########################################################################################################
def first_approach(size_t: int) -> int:
    array_list: list = []
    print("Enter the array in sorted order as binary search works only if array is sorted.")
    for i in range(size_t):
        element: int = int(input(f"Enter the {i+1} element of array :"))
        array_list.append(element)

    search_key: int = int(input("Enter the key to search :"))

    low: int = 0
    high: int = size_t - 1

    while low != high:
        mid: int = (low + high) // 2

        if search_key == array_list[mid]:
            return mid
        elif search_key > array_list[mid]:
            low = mid + 1
        elif search_key < array_list[mid]:
            high = mid - 1
    return -1


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array,))
