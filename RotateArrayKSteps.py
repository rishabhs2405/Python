"""
Problem Statement -> Given an integer array nums, rotate it to the right by k steps in-place
Reverse Entire Array 
Reverse Array till k-1
Reverse remaining part of array 
[1,2,3,4,5,6,7]
[7,6,5,4,3,2,1]
k = 3 [5,6,7,4,3,2,1]
[5,6,7,1,2,3,4]
"""

def reversing_array(arr,k):
    n = len(arr)
    k%=n 
    # reversing array in place
    def reverse(start,end):
        while start<end:
            arr[start],arr[end] = arr[end],arr[start]
            start +=1
            end -=1
    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)

arr = list(map(int,input("Enter Array elements seprated by spaces: ").split()))
k = int(input("Enter the value for which you want array rotated: "))
reversing_array(arr,k)
print("Rotated Arrau: ",arr)