"""1. Find All Indices - Linear Search
Write a function that takes an unsorted list of integers and a target value, 
and returns a list of all indices where the target appears. If target not found, 
return empty list. Time: O(n), Space: O(k) where k is occurrences.

Example:
find_all_indices([1, 3, 2, 3, 4, 3], 3) -> [1, 3, 5]
"""
def find_all_indices(arr,target):
    res = []
    for element in range(len(arr)):
        if arr[element] == target:
            res.append(element)
    return res
arr = [1, 3, 2, 3, 4, 3]
target = 3
print(f"The Indices : ",find_all_indices(arr,target))
