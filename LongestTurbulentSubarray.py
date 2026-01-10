"""
Docstring for LongestTurbulentSubarray

978. Longest Turbulent Subarray

Solved
Medium
Topics
premium lock icon
Companies

Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
 


Example 1:
Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]



Example 2:
Input: arr = [4,8,12,16]
Output: 2



Example 3:
Input: arr = [100]
Output: 1
 

Constraints:

1 <= arr.length <= 4 * 104
0 <= arr[i] <= 109
"""


# Using sliding windows to solve this problem
# arr = [9,4,2,10,7,8,8,1,9]
# arr = [9 > 4 > 2 < 10 > 7 < 8 = 8 > 1 < 9] -> res = 1, prev = '' 
#        l   r
# check if arr[r - 1] and arr[r] is alternating or having indifferences
# if arr[r - 1] < arr[r] and prev is not '<' or arr[r - 1] > arr[r] and prev is not '>'
# we update res = max(res, r - l + 1), r += 1, and prev
#
# arr = [9 > 4 > 2 < 10 > 7 < 8 = 8 > 1 < 9] -> res = 1, prev = '' 
#        l       r                           -> because arr[r-1] > arr[r] and prev = '>'  
#                                               we update l to be r - 1 and r stays
#
# arr = [9 > 4 > 2 < 10 > 7 < 8 = 8 > 1 < 9] -> res = max(2, 2 - 1 + 1) => 2, prev = '>' 
#            l   r
#
# arr = [9 > 4 > 2 < 10 > 7 < 8 = 8 > 1 < 9] -> res = max(2, 3 - 1 + 1) => 3, prev = '<' 
#            l       r
#
# arr = [9 > 4 > 2 < 10 > 7 < 8 = 8 > 1 < 9] -> res = max(3, 4 - 1 + 1) => 4, prev = '>' 
#            l            r
#
# arr = [9 > 4 > 2 < 10 > 7 < 8 = 8 > 1 < 9] -> res = max(4, 5 - 1 + 1) => 5, prev = '<' 
#            l                r
#
# arr = [9 > 4 > 2 < 10 > 7 < 8 = 8 > 1 < 9] -> res = max(4, 5 - 1 + 1) => 5, prev = '<' 
#            l                    r          -> because arr[r-1] == arr[r] we update l to 
#                                               be r and r = r + 1
#
# arr = [9 > 4 > 2 < 10 > 7 < 8 = 8 > 1 < 9] -> res = max(5, 7 - 6 + 1) => 5, prev = '<' 
#                                 l   r  
#
# arr = [9 > 4 > 2 < 10 > 7 < 8 = 8 > 1 < 9] -> res = max(5, 8 - 6 + 1) => 5, prev = '<' 
#                                 l       r  
# 
# We finish the loop and we return res = 5

def longestTurbulentSubarray(arr):
    l, r = 0, 1
    res, prev = 1, ''

    while r < len(arr):
        if arr[r - 1] > arr[r] and prev != '>':
            res = max(res, r - l + 1)
            r += 1
            prev = '>'
        elif arr[r - 1] < arr[r] and prev != '<':
            res = max(res, r - l + 1)
            r += 1
            prev = '<'
        else:
            r = r + 1 if arr[r - 1] == arr[r] else r
            l = r - 1
            prev = ''
    
    return res


arr = [9,4,2,10,7,8,8,1,9]
output = 5
lts = longestTurbulentSubarray(arr)
print(lts)
print(output)