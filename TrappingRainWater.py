"""
Problem Statement -> Given an array of non-negative integers representing elevation map heights, compute the total water trapped after raining.

each number to act as bar of that hieght in array
water gets trapped in them, where taller bars on each side(greater numbers on each side)
for each bar, find the water level above it(minimum of left and right)
"""

def trapped_water(arr):
    n = len(arr)
    if n == 0:
        return 0
    # Arrays -> Will Store maximum hieght to the left and right of each bar
    left_max = [0]*n
    right_max = [0]*n
    water = 0
    # highest bar from start to current index
    left_max[0] = arr[0]
    for i in range(1,n):
        left_max[i] = max(left_max[i-1], arr[i])
    # highest bar from end to current index    
    right_max[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        right_max[i]= max(right_max[i+1],arr[i])
    # calculating trapped water
    for i in range(n):
        water += min(left_max[i],right_max[i]) - arr[i]
        
    return water 
        
        
arr = [11,13,15,11,18,11,19,20]
res = trapped_water(arr)
print(f"The Trapped Water in {arr} is {res}.")
