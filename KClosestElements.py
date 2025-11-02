"""
658. Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]


Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]


Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""


# Using sliding windows algorithm and binary search to find the closest to x
# arr = [1,2,3,4,5], k = 4, x = 3
# output = [1,2,3,4]
# Ex
# arr = [1, 2, 3, 4, 5]  -> calculate mid point mid = (l + r) // 2 = 0
#        lm  r           -> calcualte if x - arr[m] > arr[m+k] - x = 3 - 1 > 5 - 3
#                        -> if not then slide r to be mid
# arr = [1, 2, 3, 4, 5]  -> mid = 0 + 2 // 2 = 1
#        lr              -> calculate = 3 - 2 > 4 - 3
# Exit loop cause l == r
# return arr[l:l+k]

def KClosestEl(arr, k, x):
    l, r = 0, len(arr) - k

    while l < r:
        mid = (l + r) // 2
        print(l,mid, r, x - arr[mid], arr[mid+k] - x)
        if x - arr[mid] > arr[mid + k] - x:
            l = mid + 1
        else:
            r = mid
    
    return arr[l:l+k]


arr = [1,2,3,4,5]
k = 4
x = 3
output = [1,2,3,4]
kc = KClosestEl(arr, k, x)
print(kc)
print(output)