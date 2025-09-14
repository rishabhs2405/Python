"""
    Problem Statement -> Given an integer array nums, return an array answer where answer[i] is the product of all elements in nums except nums[i].
    Prefix Product
    Suffix Product 
    Return Output Array Working for each element in array
"""

def product_array(arr):
    n = len(arr)
    result = [1]*n
    prefix = 1
    for i in range(n):
        # assigning prefix product to result[i]
        result[i] = prefix 
        prefix *= arr[i]
    suffix = 1
    for i in range(n-1,-1,-1):
        # Multiplying with Suffix product
        result[i]*= suffix
        suffix *= arr[i]
    
    return result

arr = [1,2,3,4,5,6,7,8,9,10]
print(f"The Product Array of {arr} is: {product_array(arr)}")