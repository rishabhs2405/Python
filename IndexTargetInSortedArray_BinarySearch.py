# Problem Statement -> Implement binary search in Python to find the index of a target in a sorted array.

def Find_Index(arr,target):
    left,right = 0, len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            left = mid + 1
        else:
            right = mid -1 
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
target = 5
index = Find_Index(arr,target)
if index != -1:
    print(f"The position of {target} in {arr} is: {index + 1}")
else:
    print(f"{target} not found in {arr}")




    