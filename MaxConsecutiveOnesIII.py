"""
1004. Max Consecutive Ones III

Solved
Medium
Topics
premium lock icon
Companies
Hint

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.




Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""


# Using Sliding Windows with time: O(n) and space: O(1)

def longestOnes(nums, k):
    res = 0
    l = 0

    for r in range(len(nums)):
        k -= 1 if nums[r] == 0 else 0
        while k < 0:
            k += 1 if nums[l] == 0 else 0
            l += 1
        res = max(res, (r - l + 1))

    return res

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
output = 10

res = longestOnes(nums, k)

print(res)
print(output)