########################################################################################################
# Question: sort the elements in an array ASC

# Implement a program to sort the given array elements in ASC order.

# input -----> size and array elements
# con -------> size<100
# output ----> sorted array in ASC

# Logic:
# ~~~~~~
# 3,1,4,2,5
# 1,3,4,2,5
# 1,2,4,3,5
# 1,2,3,4,5

# for(i=0;i<n;i++){
# 	for(j=i+1;j<n;j++){
# 	if(a[i]>a[j]){
# 	t=a[i];
# 	a[i]=a[j];
# 	a[j]=t;
# 	}
# 	}
# }
########################################################################################################
from typing import Tuple


def swap(x: int, y: int) -> Tuple[int, int] :
    return y, x


def first_approach(size_t: int) -> list:
    array_list: list = []
    for i in range(size_t):
        element: int = int(input(f"Enter the {i+1} element of array :"))
        array_list.append(element)

    for i in range(len(array_list)):
        for j in range(i+1, len(array_list)):
            if array_list[i] > array_list[j]:
                array_list[i], array_list[j] = swap(array_list[i], array_list[j])
    return array_list


if __name__ == "__main__":
    size_of_array: int = int(input("Enter the size of array :"))
    print(first_approach(size_of_array,))
