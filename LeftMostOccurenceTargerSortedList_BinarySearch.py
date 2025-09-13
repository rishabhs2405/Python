"""
2. First Occurrence - Binary Search
Implement binary search to find the leftmost (first) occurrence of a target 
in a sorted list that may contain duplicates. Return index or -1 if not found.
Time: O(log n)
"""

def find_left_index(arr,target):
    left,right = 0, len(arr) -1 
    res = -1
    while left<=right:
        mid = (left + right) //2
        if arr[mid] == target:
            res = mid
            right = mid -1
        elif arr[mid]<target:
            left = mid + 1
        else:
            right = mid + 1
    return res
            
arr = [1,1,1,2,2,2,4,5,6,11,12]
target = 2
result = find_left_index(arr,target)
print(result)