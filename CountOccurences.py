"""
3. Count Occurrences - Binary Search
Using binary search, count how many times a target appears in a sorted list 
with possible duplicates. Return 0 if not found. Time: O(log n)

Example:
count_occurrences([1, 2, 2, 2, 3, 4], 2) -> 3
"""
def find_counts(arr,target):
    left,right = 0, len(arr)-1
    counts = 0
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target:
            counts +=1
            right = mid -1
        elif arr[mid] < target:
            left = mid + 1
        else :
            right = mid - 1
    return counts
    
arr = [1,2,2,2,3,4]
target = 2
counts = find_counts(arr,target)
print(f"The Counts of {target} in {arr} is :{counts}")