"""
4. Find Max Element - Linear Search
Write a linear search to find the index of the maximum element in an unsorted 
list of integers. If list empty, return None. Time: O(n)

Example:
find_max_element([3, 1, 4, 1, 5, 9, 2]) -> 5  # index of 9
"""

def find_maximum(arr):
    if not arr:
        return None
    max_index = 0
    for i in range(1,len(arr)):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index
arr = [3,1,4,1,5,9,2]
print(find_maximum(arr))