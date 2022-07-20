########################################################################################################
# Question: search for an element in an array

# Implement a program to search for an element in an array.

# input -------> size, array elements and element to search
# con ---------> size<100
# output ------> search for the given element and return index

# 5
# 1 2 3 5 4

# 1 ----> 0
# 2 ----> 1
# 3 ----> 2
# 5 ----> 3
# 4 ----> 4
# 6 ----> -1

# Logic:
# ~~~~~~
# index=-1;
# for(i=0;i<n;i++){
# 	if(key==a[i]){
# 		index=i;
# 		break;
# 	}
# }

# printf("%d",index);
########################################################################################################
def first_approach(size_t: int) -> int:
    array_list: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i+1} element of array :"))
        array_list.append(element)
    search_ele: int = int(input("Enter the search element :"))

    for i, element in enumerate(array_list):
        if element == search_ele:
            return i

    return -1


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array,))
