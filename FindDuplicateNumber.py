"""
Problem Statement -> Find the Duplicate Number: Given an array nums of n+1 integers in [1,n] with one duplicate, find the repeated number using O(1) space.

Floyd's tortoise and hare algorithm -> two pointer algorithm moving through sequence at different speeds. ALgorithm is used to find the loop in liked list
faster one is called the fast pointer and other one is called slow pointer.
fast moves twice as the slow pointer.
slow pointer will move one step at a time
fast pointer will move two steps at a time
if thereis a cycle, fast pointer will eventualy catchup with the slow pointer because its moving faster
if no cycle, fast pointer will reach the end of list i.e. it will become null


Avoids need of Extra Space 
"""
def find_duplicates(nums):
    slow = nums[0]
    fast = nums[0]
    while True:
        # Moving Slow pointer by 1 step
        slow = nums[slow]
        # Moving Fast pointer by 2 steps
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # Find the duplicate i.e. cycle entry point
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
nums = [1,3,4,2,5,6,2]
print(f"Duplicate Number: {find_duplicates(nums)}")